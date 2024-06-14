import json
from time import sleep
from kafka import KafkaProducer


# Serializador para Kafka Producer
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:29092', 'localhost:39092', 'localhost:49092'],
    value_serializer=serializer
)


def get_push_records():
    with open('../cities.json', 'r') as file:
        cities = json.load(file)

    debug = True
    for city in cities:
        if debug:
            print(f"Sending record to Kafka: {city}")
            if 'timestamp' in city:
                print(city["timestamp"])

        producer.send('my-topic', city)
    producer.flush()


def main():
    while True:
        get_push_records()
        sleep(2)


if __name__ == "__main__":
    main()
