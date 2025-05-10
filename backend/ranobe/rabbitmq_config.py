import pika

RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = 'ranobe_queue'

def get_rabbitmq_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    return connection
