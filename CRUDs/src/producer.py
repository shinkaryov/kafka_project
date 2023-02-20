from kafka import KafkaProducer
import json


class Producer:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='kafka:9092', api_version=(0, 10, 1),
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def send_value(self, topic, value):
        self.producer.send(topic, value)
        self.producer.flush()

    def close(self):
        self.producer.close()


# producer initialization
producer = Producer()
