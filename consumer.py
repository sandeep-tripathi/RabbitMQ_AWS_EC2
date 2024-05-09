import pika

# Connect to RabbitMQ server on AWS EC2 instance
connection = pika.BlockingConnection(pika.ConnectionParameters('YOUR_EC2_PUBLIC_IP'))
channel = connection.channel()

# Declare a queue named 'myqueue'
channel.queue_declare(queue='myqueue')

# Consumer
def callback(ch, method, properties, body):
    print(" [x] Received:", body.decode())

# Set up consumer
channel.basic_consume(queue='myqueue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
