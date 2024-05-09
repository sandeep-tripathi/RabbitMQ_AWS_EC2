import pika
import ssl

# Connection parameters for RabbitMQ on EC2 for consumer
#ec2_public_ip = 'YOUR_EC2_PUBLIC_IP'   # Replace 'YOUR_EC2_PUBLIC_IP'
credentials = pika.PlainCredentials('myuser', 'mypassword')

#  AWS is using AMQPS, you should add ssl_options to your connection parameters
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
parameters = pika.ConnectionParameters(host='a-25c34e4d-a3eb-32de-abfg-l95d931afc72f.mq.eu-central-1.amazonaws.com',
                                       port=5671,
                                       virtual_host='/',
                                       credentials=credentials,
                                       ssl_options=pika.SSLOptions(context)
                                       )


# Declare a queue named 'myqueue'
channel.queue_declare(queue='myqueue')

# Consumer
def callback(ch, method, properties, body):
    print(" [x] Received:", body.decode())

# Set up consumer
channel.basic_consume(queue='myqueue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
