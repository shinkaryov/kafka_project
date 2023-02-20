from kafka import KafkaConsumer
import json
from engine import db
from producer import Producer
from check import check_state


class Consumer:
    def __init__(self, topic, group_id):
        self.consumer = KafkaConsumer(topic, bootstrap_servers='kafka:9092', auto_offset_reset='earliest',\
                                      api_version=(0, 10, 1), group_id=group_id, \
                                      value_deserializer=lambda m: json.loads(m.decode('ascii')))
        self.producer = Producer()

    def run(self):
        for msg in self.consumer:
            value = msg.value   # get value from topic
            bets = db.execute("SELECT * FROM Bets " + \
                              f"WHERE event_id = '{value['id']}';").all()  # get all bets from db with defined event
            # iterating bets and sending it to topic "bets.state"
            for bet in bets:
                state = check_state(value['score'], value['state'], bet['market'])
                new_bet = {
                    'id': bet['id'],
                    'date': str(bet['date']),
                    'user_id': bet['user_id'],
                    'event_id': bet['event_id'],
                    'market': bet['market'],
                    'state': state
                }
                self.producer.send_value('bets.state', new_bet)

    def close(self):
        self.consumer.close()
        self.producer.close()


# initializing and running consumer BetScorer
BetScorer = Consumer('events.taxonomy', 'bet_scorer')
BetScorer.run()
