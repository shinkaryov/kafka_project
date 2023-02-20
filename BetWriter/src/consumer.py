from kafka import KafkaConsumer
import json
from engine import db


class Consumer:
    def __init__(self, topic, group_id):
        self.consumer = KafkaConsumer(topic, bootstrap_servers='kafka:9092', auto_offset_reset='earliest',\
                                      api_version=(0, 10, 1), group_id=group_id, \
                                      value_deserializer=lambda m: json.loads(m.decode('ascii')))

    def run(self):
        for msg in self.consumer:
            value = msg.value
            # updating state of bets
            db.execute("UPDATE Bets " + \
                        "SET " + \
                        f"state = '{value['state']}' "
                        f"WHERE id = '{value['id']}';")

    def close(self):
        self.consumer.close()


# initializing and running consumer BetWriter
BetWriter = Consumer('bets.state', 'bet_writer')
BetWriter.run()
