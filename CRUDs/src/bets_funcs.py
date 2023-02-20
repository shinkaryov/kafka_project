from engine import db
from Bets import Bet


# creating table Bets and adding some values into it
def create_table_bets():
    query = "" + \
            "CREATE TABLE IF NOT EXISTS Bets (" + \
            "id INT UNIQUE NOT NULL, " + \
            "date DATE, " + \
            "user_id VARCHAR(50), " + \
            "event_id INT NOT NULL, " + \
            "market VARCHAR(10), " + \
            "state VARCHAR (10));"
    db.execute(query)
    if db.execute(f"SELECT 1 FROM Bets WHERE id = '1'").all() == []:
        db.execute("INSERT INTO Bets (id,date,user_id,event_id,market,state) " + \
                   "VALUES (" + \
                   "'1', '2022-12-02', 'Thomas1665070563', '1', 'team_2', 'win');")
    if db.execute(f"SELECT 1 FROM Bets WHERE id = '2'").all() == []:
        db.execute("INSERT INTO Bets (id,date,user_id,event_id,market,state) " + \
                   "VALUES (" + \
                   "'2', '2022-12-02', 'Thomas1665070563', '2', 'team_2', 'lose');")
    if db.execute(f"SELECT 1 FROM Bets WHERE id = '3'").all() == []:
        db.execute("INSERT INTO Bets (id,date,user_id,event_id,market,state) " + \
                   "VALUES (" + \
                   "'3', '2022-12-02', 'Thomas1665070563', '3', 'team_1', 'win');")
    if db.execute(f"SELECT 1 FROM Bets WHERE id = '4'").all() == []:
        db.execute("INSERT INTO Bets (id,date,user_id,event_id,market,state) " + \
                   "VALUES (" + \
                   "'4', '2022-12-02', 'Thomas1665070563', '4', 'draw', 'lose');")
    if db.execute(f"SELECT 1 FROM Bets WHERE id = '5'").all() == []:
        db.execute("INSERT INTO Bets (id,date,user_id,event_id,market,state) " + \
                   "VALUES (" + \
                   "'5', '2022-12-03', 'Thomas1665070563', '5', 'team_1', 'win');")


# creating new bet
def new_bet(bet: Bet):
    # checking user existence
    cond1 = (db.execute("SELECT * FROM Users " + \
                        "WHERE id = " + f"'{bet.user_id}'" + ";").all() != [])
    # checking event existence and its state
    cond2 = (db.execute("SELECT * FROM Events " + \
                        "WHERE id = " + f"'{bet.event_id}'" + "AND state = 'created';").all() != [])
    # checking uniqueness of bet id
    cond3 = (db.execute(f"SELECT 1 FROM Bets WHERE id = '{bet.id}'").all() == [])
    if cond1 and cond2 and cond3:
        db.execute("INSERT INTO Bets (id,date,user_id,event_id, market, state) " + \
                   "VALUES (" + \
                   f"'{bet.id}', '{bet.date}', '{bet.user_id}', '{bet.event_id}', '{bet.market}', 'None');")
        return db.execute("SELECT * FROM Bets " + \
                          "WHERE id = " + f"'{bet.id}'" + ";").all()
    else:
        return ValueError('Cannot post a bet - input error')


# updating bet
def change_bet(bet: Bet):
    # checking user existence
    cond1 = (db.execute("SELECT * FROM Users " + \
                        "WHERE id = " + f"'{bet.user_id}'" + ";").all() != [])
    # checking event existence
    cond2 = (db.execute("SELECT * FROM Events " + \
                        "WHERE id = " + f"'{bet.event_id}'" + ";").all() != [])
    # checking existence of the bet
    cond3 = (db.execute(f"SELECT 1 FROM Bets WHERE id = '{bet.id}'").all() != [])
    if cond1 and cond2 and cond3:
        db.execute("UPDATE Bets " + \
                   "SET " + \
                   f"date = '{bet.date}'," + \
                   f"user_id = '{bet.user_id}'," + \
                   f"event_id = '{bet.event_id}' " + \
                   f"WHERE id = '{bet.id}';")
        return db.execute("SELECT * FROM Bets " + \
                          "WHERE id = " + f"'{bet.id}'" + ";").all()
    else:
        return ValueError('Cannot change the bet - wrong input')