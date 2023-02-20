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
            # getting message from topic and create or update event
            value = msg.value
            if db.execute(f"SELECT 1 FROM Events WHERE id = '{value['id']}'").all() == []:
                db.execute("INSERT INTO Events (id,type,team_1,team_2,event_date,score,state) " + \
                           "VALUES (" + \
                           f"'{value['id']}', '{value['type']}', '{value['team_1']}', '{value['team_2']}', " + \
                           f"'{value['event_date']}', '{value['score']}', '{value['state']}');")
            else:
                db.execute("UPDATE Events " + \
                           "SET " + \
                           f"score = '{value['score']}'," + \
                           f"state = '{value['state']}' " + \
                           f"WHERE id = '{value['id']}';")

    def close(self):
        self.consumer.close()


# initializing and running consumer EventsWriter
EventsWriter = Consumer('events.taxonomy', 'events_writer')
EventsWriter.run()
