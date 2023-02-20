from Events import Event
from engine import db
from producer import producer
import time


# creation of table Events and inserting here few values
def create_table_events():
    query = "" + \
            "CREATE TABLE IF NOT EXISTS Events (" + \
                "id INT UNIQUE NOT NULL, " + \
                "type VARCHAR(50), " + \
                "team_1 VARCHAR(50), " + \
                "team_2 VARCHAR(50), " + \
                "event_date DATE, " + \
                "score VARCHAR(20), " + \
                "state VARCHAR(20));"
    db.execute(query)
    if db.execute(f"SELECT 1 FROM Events WHERE id = '1'").all() == []:
        db.execute("INSERT INTO Events (id,type,team_1,team_2,event_date,score,state) " + \
                   "VALUES (" + \
                   "'1', 'football', 'Ghana', 'Uruguay', '2022-12-02', '0-2', 'finished');")
    if db.execute(f"SELECT 1 FROM Events WHERE id = '2'").all() == []:
        db.execute("INSERT INTO Events (id,type,team_1,team_2,event_date,score,state) " + \
                   "VALUES (" + \
                   "'2', 'football', 'South Korea', 'Portugal', '2022-12-02', '2-1', 'finished');")
    if db.execute(f"SELECT 1 FROM Events WHERE id = '3'").all() == []:
        db.execute("INSERT INTO Events (id,type,team_1,team_2,event_date,score,state) " + \
                   "VALUES (" + \
                   "'3', 'football', 'Cameroon', 'Brazil', '2022-12-02', '1-0', 'finished');")
    if db.execute(f"SELECT 1 FROM Events WHERE id = '4'").all() == []:
        db.execute("INSERT INTO Events (id,type,team_1,team_2,event_date,score,state) " + \
                   "VALUES (" + \
                   "'4', 'football', 'Serbia', 'Switzerland', '2022-12-02', '1-2', 'finished');")
    if db.execute(f"SELECT 1 FROM Events WHERE id = '5'").all() == []:
        db.execute("INSERT INTO Events (id,type,team_1,team_2,event_date,score,state) " + \
                   "VALUES (" + \
                   "'5', 'football', 'Netherlands', 'USA', '2022-12-03', '3-1', 'finished');")


# creation of new event
def new_event(event: Event):
    if db.execute(f"SELECT 1 FROM Events WHERE id = '{event.id}'").all() == []:
        # if such event doesn't exist, send it to topic "events.taxonomy"
        producer.send_value('events.taxonomy', event.dict())
        time.sleep(3)
        return db.execute("SELECT * FROM Events " + \
                          "WHERE id = " + f"'{event.id}'" + ";").all()
    else:
        return 'Creation Error:' \
               'Such event already exists'


# updating of event
def change_event(event: Event):
    if db.execute(f"SELECT 1 FROM Events WHERE id = '{event.id}'").all() == []:
        return 'Error: no such event'
    else:
        # if such event exists, send it to topic "events.taxonomy"
        producer.send_value('events.taxonomy', event.dict())
        time.sleep(3)
        return db.execute("SELECT * FROM Events " + \
                          "WHERE id = " + f"'{event.id}'" + ";").all()
