from engine import db
from preprocessing import prepare_data
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    time_created: int
    gender: Optional[str] = None
    age: Optional[int] = 30
    last_name: Optional[str] = None
    ip: Optional[str] = None
    city: Optional[str] = None
    premium: Optional[bool] = False
    birth_day: Optional[str] = None
    balance: Optional[float] = 0


# creation of table Users and insertion of data from jsonl file
def create_table_users():
    query = "" + \
            "CREATE TABLE IF NOT EXISTS Users (" + \
                "id VARCHAR(50) UNIQUE NOT NULL," + \
                "name VARCHAR(20) NOT NULL," + \
                "last_name VARCHAR(20)," + \
                "time_created INT NOT NULL," + \
                "gender VARCHAR(10)," + \
                "age INT," + \
                "ip VARCHAR(20)," \
                "city VARCHAR(20)," + \
                "premium BOOL," + \
                "balance DECIMAL(10, 2)" + \
            ");"
    db.execute(query)
    data = prepare_data('data.jsonl')
    for key in data:
        if db.execute(f"SELECT 1 FROM Users WHERE id = '{key}'").all() == []:
            db.execute("INSERT INTO Users (id,name,last_name,time_created,gender,age,ip,city,premium,balance) " + \
                       "VALUES (" + \
                       f"'{key}'," + \
                       f"'{data[key]['name']}'," + \
                       f"'{data[key]['last_name']}'," + \
                       f"'{data[key]['time_created']}'," + \
                       f"'{data[key]['gender']}'," + \
                       f"'{data[key]['age']}'," + \
                       f"'{data[key]['ip']}'," + \
                       f"'{data[key]['city']}'," + \
                       f"'{data[key]['premium']}'," + \
                       f"'{data[key]['balance']}');")


# creation of new user
def new_user(user: User):
    user_id = user.name + str(user.time_created)
    if db.execute(f"SELECT 1 FROM Users WHERE id = '{user_id}'").all() == []:
        db.execute("INSERT INTO Users (id,name,last_name,time_created,gender,age,ip,city,premium,balance) " + \
                   "VALUES (" + \
                   f"'{user_id}'," + \
                   f"'{user.name}'," + \
                   f"'{user.last_name}'," + \
                   f"'{user.time_created}'," + \
                   f"'{user.gender}'," + \
                   f"'{user.age}'," + \
                   f"'{user.ip}'," + \
                   f"'{user.city}'," + \
                   f"'{user.premium}'," + \
                   f"'{user.balance}');")
        return db.execute("SELECT * FROM Users " + \
                          "WHERE id = " + f"'{user_id}'" + ";").all()
    else:
        return 'Creation Error:' \
               'Such user already exists'


# changing of user
def change_user(user: User):
    user_id = user.name + str(user.time_created)
    if db.execute(f"SELECT 1 FROM Users WHERE id = '{user_id}'").all() == []:
        return 'Error: no such user'
    else:
        db.execute("UPDATE Users " + \
                   "SET " + \
                   f"last_name = '{user.last_name}'," + \
                   f"gender = '{user.gender}'," + \
                   f"age = '{user.age}'," + \
                   f"ip = '{user.ip}'," + \
                   f"city = '{user.city}'," + \
                   f"premium = '{user.premium}'," + \
                   f"balance = '{user.balance}' " + \
                   f"WHERE id = '{user_id}';")
        return db.execute("SELECT * FROM Users " + \
                          "WHERE id = " + f"'{user_id}'" + ";").all()


