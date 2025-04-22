import pika

params = pika.URLParameters('amqps://aqucbhji:jGfQm9Ycpi7AjxY8S_rHJPpsIiLMZDu1@leopard.lmq.cloudamqp.com/aqucbhji')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='Hello 2')
