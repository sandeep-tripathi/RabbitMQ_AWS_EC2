import pika

# Connection parameters for RabbitMQ on EC2 for producer
ec2_public_ip = 'YOUR_EC2_PUBLIC_IP'   # Replace 'YOUR_EC2_PUBLIC_IP' with the actual public IP address of your EC2 instance
credentials = pika.PlainCredentials('myuser', 'mypassword')
parameters = pika.ConnectionParameters(ec2_public_ip, 5672, '/', credentials)

connection = pika.BlockingConnection(parameters)
#connection = pika.BlockingConnection(pika.ConnectionParameters(''amqp://myuser:mypassword@your-ec2-instance-public-ip''))

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
