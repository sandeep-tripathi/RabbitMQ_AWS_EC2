import pika

# Connect to RabbitMQ server on AWS EC2 instance
connection = pika.BlockingConnection(pika.ConnectionParameters('YOUR_EC2_PUBLIC_IP'))
channel = connection.channel()

# Declare a queue named 'myqueue'
channel.queue_declare(queue='myqueue')

# Producer
def send_message(message):
    channel.basic_publish(exchange='', routing_key='myqueue', body=message)
    print(" [x] Sent:", message)

# Example messages
messages = ["Hello", "RabbitMQ", "Producer"]

# Send each message
for message in messages:
    send_message(message)

# Close the connection
connection.close()
