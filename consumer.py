import pika

# Connection parameters for RabbitMQ on EC2 for consumer
ec2_public_ip = 'YOUR_EC2_PUBLIC_IP'   # Replace 'YOUR_EC2_PUBLIC_IP' with the actual public IP address of your EC2 instance
credentials = pika.PlainCredentials('myuser', 'mypassword')   # User named myuser should already created 
parameters = pika.ConnectionParameters(ec2_public_ip, 5672, '/', credentials)

# Declare a queue named 'myqueue'
channel.queue_declare(queue='myqueue')

# Consumer
def callback(ch, method, properties, body):
    print(" [x] Received:", body.decode())

# Set up consumer
channel.basic_consume(queue='myqueue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
