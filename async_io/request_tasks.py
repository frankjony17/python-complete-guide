"""
The cats (nodejs usually, can be used for other languages too)

Imagine want to grab 22 JSON structures of cats from this api -> https://cataas.com/cat?json=true,
which returns a single random cat image JSON, without fetching more than 3 concurrently -
that is, you can only have 3 concurrent HTTPS requests running at a time, but you should still
optimize for speed.

The API returns a random JSON structure that represents a cute cat picture.
The problem is similar to one we run into all the time: Upload 10's of thousands of images to
AWS S3, for example, without exceeding the limits of the network on the machine doing the uploading.

{
  "id": "62d543dd5e0a3e0018eca910",
  "created_at": "2022-07-18T11:28:29.596Z",
  "tags": [
    "two",
    "double",
    "black"
  ],
  "url": "/cat/62d543dd5e0a3e0018eca910"
}
"""
import asyncio
import requests


async def make_request(url):
    print("Starting to make a requests")
    return requests.get(url)


async def main():
    url = "https://cataas.com/cat?json=true"
    count = 22

    while count > 0:
        task_1 = asyncio.create_task(make_request(url))
        task_2 = asyncio.create_task(make_request(url))
        task_3 = asyncio.create_task(make_request(url))

        await task_1
        await task_2
        await task_3

        count -= 3
    print("Ending requests")

asyncio.run(main())
