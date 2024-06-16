from kafka import KafkaConsumer
from concurrent.futures import ThreadPoolExecutor


def consume_messages(consumer, consumer_id):
    for message in consumer:
        print(
            f"[{consumer_id}]: {message.topic}:{message.partition}:{message.offset}: key={message.key} value={message.value}")


def create_consumer(group_id):
    return KafkaConsumer('my-topic',
                         group_id=group_id,
                         api_version=(0, 10),
                         bootstrap_servers=['localhost:29092', 'localhost:39092', 'localhost:49092'])


# Crear consumidores con different IDs de grupo
consumer1 = create_consumer('my-group-1')
consumer2 = create_consumer('my-group-2')

# Ejecutar consumidores en paralelo
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(consume_messages, consumer1, 1)
    executor.submit(consume_messages, consumer2, 2)
