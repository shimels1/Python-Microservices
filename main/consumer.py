import pika

params = pika.URLParameters('amqps://aqucbhji:jGfQm9Ycpi7AjxY8S_rHJPpsIiLMZDu1@leopard.lmq.cloudamqp.com/aqucbhji')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main', durable=True)

def callback(ch,method, properties, body):
    print('Received in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Starte consuming')

channel.start_consuming()
channel.close()
