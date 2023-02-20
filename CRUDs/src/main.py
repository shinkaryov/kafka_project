from fastapi import FastAPI
from engine import db
import logging
from Users import create_table_users, User, new_user, change_user
from Bets import Bet
from bets_funcs import create_table_bets, new_bet, change_bet

LOGGER = logging.getLogger(__name__)

# app and db inizialization
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    create_table_users()
    create_table_bets()


# CRUDs for Users

@app.get("/users")
async def get_all_users():
    return db.execute("SELECT * FROM Users;").all()


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return db.execute("SELECT * FROM Users " + \
                      "WHERE id = " + f"'{user_id}'" + ";").all()


@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    db.execute("DELETE FROM Users " + \
               "WHERE id = " + f"'{user_id}'" + ";")


@app.delete("/users")
async def delete_all_users():
    db.execute("DELETE FROM Users")


@app.post("/users/{user_id}")
async def create_user(user: User):
    return new_user(user)


@app.put("/users/{user.name + str(user.time_created)}")
async def update_user(user: User):
    return change_user(user)


# CRUDs for Bets

@app.get("/bets")
async def get_all_bets():
    return db.execute("SELECT * FROM Bets;").all()


@app.get("/bets/{bet_id}")
async def get_bet(bet_id: int):
    return db.execute("SELECT * FROM Bets " + \
                      "WHERE id = " + f"'{bet_id}'" + ";").all()


@app.delete("/bets/{bet_id}")
async def delete_bet(bet_id: str):
    db.execute("DELETE FROM Bets " + \
               "WHERE id = " + f"'{bet_id}'" + ";")


@app.delete("/bets")
async def delete_all_bets():
    db.execute("DELETE FROM Bets")


@app.post("/bets/{bet.id}")
async def create_bet(bet: Bet):
    return new_bet(bet)


@app.put("/bets/{bet.id}")
async def update_bet(bet: Bet):
    return change_bet(bet)
