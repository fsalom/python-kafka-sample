from kafka import KafkaConsumer

consumer = KafkaConsumer(api_version=(0, 10),
                         bootstrap_servers=['localhost:29092', 'localhost:39092', 'localhost:49092'])
consumer.subscribe(pattern='^my-topic.*', )

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
