from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'orders_project',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_commit_interval_ms=3000
)

try:
    for message in consumer:
        #print(message)
        print(json.dumps(message.value, indent=4))

except KeyboardInterrupt:
    print('Closing')
finally:
    consumer.close()

