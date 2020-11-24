import asyncio
import aio_pika


async def main(loop):
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@192.168.20.241/", loop=loop
    )

    async with connection:
        routing_key = "test"

        channel = await connection.channel()

        for i in range(100000):
            await channel.default_exchange.publish(
                aio_pika.Message(body=f"Hello {i}".encode()),
                routing_key=routing_key,
            )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()