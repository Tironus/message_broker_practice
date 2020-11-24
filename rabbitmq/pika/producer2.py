import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.20.241'))
channel = connection.channel()
channel.queue_declare(queue='test')
for i in range(100000):
    channel.basic_publish(
        exchange='',
        routing_key='test',
        body=f'Test message {i}.'
    )
    print('sent Test message')
connection.close()