import json

from kafka import KafkaConsumer

consumer = KafkaConsumer('my-topic',
                         api_version=(0, 10),
                         bootstrap_servers=['localhost:29092', 'localhost:39092', 'localhost:49092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         value_deserializer=lambda m: json.loads(m.decode('ascii')),
                         consumer_timeout_ms=1000)

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
