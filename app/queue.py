import pika
import json

def publish_message(application_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='loan_queue')
    channel.basic_publish(exchange='', routing_key='loan_queue', body=json.dumps({'application_id': application_id}))
    connection.close()

def consume_messages(callback):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='loan_queue')
    channel.basic_consume(queue='loan_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def process_application(ch, method, properties, body):
    application_data = json.loads(body)
    application_id = application_data['application_id']
    # Process application here
