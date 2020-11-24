import aio_pika
import asyncio

async def main(loop):
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@192.168.20.241/", loop=loop
    )

    queue_name = "test"

    async with connection:
        # Creating channel
        channel = await connection.channel()

        # Declaring queue
        queue = await channel.declare_queue(queue_name)

        while True:
            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    async with message.process():
                        print(message.body)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()