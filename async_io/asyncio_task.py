import asyncio
import random
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main_1():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

# asyncio.run(main_1())  # 3 seconds


async def main_2():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


# asyncio.run(main_2())  # 2 seconds

"""
    Creating Tasks
"""


async def main_3():
    background_tasks = set()

    for i in range(10):
        r = random.randint(1, 3)

        task = asyncio.create_task(say_after(r, f'hello - {r}s'), name=f"task-{i}")

        # Add task to the set. This creates a strong reference.
        background_tasks.add(task)

        # To prevent keeping references to finished tasks forever,
        # make each task remove its own reference from the set after
        # completion:
        task.add_done_callback(background_tasks.discard)

    print(f"started at {time.strftime('%X')}")

    await asyncio.gather(*background_tasks)

    print(f"finished at {time.strftime('%X')}")

    print(background_tasks)

asyncio.run(main_3())  # 2 seconds

