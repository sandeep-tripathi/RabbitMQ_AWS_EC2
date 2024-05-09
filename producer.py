import pika
import ssl

# Connection parameters for RabbitMQ on EC2 for producer
#ec2_public_ip = 'YOUR_EC2_PUBLIC_IP'   # Replace 'YOUR_EC2_PUBLIC_IP' with the actual public IP address of your EC2 instance
credentials = pika.PlainCredentials('myuser', 'mypassword')
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
parameters = pika.ConnectionParameters(host='a-25c34e4d-a3eb-32de-abfg-l95d931afc72f.mq.eu-central-1.amazonaws.com',
                                       port=5671,
                                       virtual_host='/',
                                       credentials=credentials,
                                       ssl_options=pika.SSLOptions(context)
                                       )


connection = pika.BlockingConnection(parameters)


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
