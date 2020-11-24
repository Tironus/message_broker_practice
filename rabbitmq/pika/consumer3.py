import pika

while True:
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.20.241'))
    channel = connection.channel()
    channel.queue_declare(queue='test')
    for method_frame, properties, body in channel.consume('test'):
        # Display the message parts and acknowledge the message
        print(method_frame, properties, body)
        channel.basic_ack(method_frame.delivery_tag)

    # Cancel the consumer and return any pending messages
    requeued_messages = channel.cancel()
    print('Requeued %i messages' % requeued_messages)
    connection.close()