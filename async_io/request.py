import asyncio
import json

import httpx
from fastapi import status
from loguru import logger

from matriz_antifraude.config.settings import (BASIC_HEADERS, MAX_ATTEMPTS,
                                               REQUEST_TIMEOUT, TIME_SLEEP,
                                               VERIFY)
from matriz_antifraude.exception.custom import (APIError,
                                                ServiceBadRequestException,
                                                ServiceNotFoundException,
                                                ServiceRequestException,
                                                ServiceUnauthorizedException)


class RequestApi:
    def __init__(self, url, headers=None, token=None):
        self.url = url
        if headers is None:
            self.headers = BASIC_HEADERS
        else:
            self.headers = headers
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    async def make_request(self, payload, verify=VERIFY, timeout=REQUEST_TIMEOUT, dumps=True):
        for attempt in range(MAX_ATTEMPTS):
            logger.info(f'[+] Sending request to {self.url}, attempt #{attempt + 1}')
            response = await self.post_request(payload, attempt, verify, timeout, dumps)

            if response:
                return response

            logger.warning(f'[*] Request failed. Waiting {TIME_SLEEP}s before new attempt.')
            await asyncio.sleep(TIME_SLEEP)
        raise APIError(error="The request could not be made, 'MAX_ATTEMPTS' not configured.")

    async def post_request(self, payload, attempt, verify, timeout, dumps):
        try:
            async with httpx.AsyncClient(verify=verify) as client:
                payload = json.dumps(payload) if dumps else payload
                response = await client.post(
                    url=self.url, data=payload, headers=self.headers, timeout=timeout)

            if 500 <= response.status_code <= 599:
                response.raise_for_status()

            logger.info(f'[*] Request for [{self.url}] - [StatusCode={response.status_code}]')
            return self.process_response(response)
        except (httpx.ConnectError, httpx.TimeoutException,
                httpx.HTTPStatusError, AttributeError, TypeError) as exc:
            logger.error(f'[-] Exception - [URL={self.url}] - [ERROR={self.__get_error(exc)}]')
            if attempt == MAX_ATTEMPTS - 1:
                raise APIError(f'[URL={self.url}] - [ERROR={self.__get_error(exc)}]')
            return False

    def process_response(self, response):
        if response.status_code == status.HTTP_200_OK:
            return response.json()
        if response.status_code == status.HTTP_201_CREATED:
            return response.content
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise ServiceBadRequestException(url=self.url, response=response.text)
        if response.status_code == status.HTTP_404_NOT_FOUND:
            raise ServiceNotFoundException(url=self.url, response=response.text)
        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            raise ServiceUnauthorizedException(url=self.url, response=response.text)
        raise ServiceRequestException(url=self.url, exc=response.text)

    @staticmethod
    def __get_error(exc):
        try:
            return exc.response.text
        except AttributeError:
            return str(exc)
