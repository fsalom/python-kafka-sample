import json
from time import sleep
from kafka import KafkaProducer
from concurrent.futures import ThreadPoolExecutor


def serializer(message):
    return json.dumps(message).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['localhost:29092', 'localhost:39092', 'localhost:49092'],
    value_serializer=serializer
)


def flatten_record(city):
    return city


def get_push_records():
    with open('../cities.json', 'r') as file:
        cities = json.load(file)

    debug = True
    with ThreadPoolExecutor(max_workers=16) as executor:
        future_results = [executor.submit(flatten_record, city) for city in cities]

        for future in future_results:
            flat_record = future.result()
            if debug:
                print(f"Sending record to Kafka: {flat_record}")
                if 'timestamp' in flat_record:
                    print(flat_record["timestamp"])

            producer.send('my-topic', flat_record)
    producer.flush()


def main():
    while True:
        get_push_records()
        sleep(2)


if __name__ == "__main__":
    main()
