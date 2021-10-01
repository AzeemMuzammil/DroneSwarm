import asyncio

# async def test():
#     await asyncio.sleep(3)


# asyncio.run(test())

async def get_chat_id(name):
    await asyncio.sleep(3)
    return name


async def main():
    a = await get_chat_id("azzeem")
    print(a)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


'''
    {
        "taskType": "WAIT",
        "taskMode": "SEQ",
        "taskId": 2,
        "preConditions": [
            {
                "preConditionTaskId": 1,
                "preConditionTaskStatus": "END"
            }
        ],
        "waitTime": 3.0
    },
    '''