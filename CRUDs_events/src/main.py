from fastapi import FastAPI
from engine import db
import logging
from events_funcs import create_table_events, new_event, change_event
from Events import Event
from typing import List

LOGGER = logging.getLogger(__name__)

# app initialization
app = FastAPI()


# CRUDs for events


@app.on_event("startup")
async def startup_event():
    create_table_events()


@app.get("/events")
async def get_all_events()->List[Event]:
    return db.execute("SELECT * FROM Events;").all()


@app.get("/events/{event_id}")
async def get_event(event_id: int)->Event:
    return db.execute("SELECT * FROM Events " + \
                      "WHERE id = " + f"'{event_id}'" + ";").all()


@app.delete("/events/{event_id}")
async def delete_event(event_id: str):
    db.execute("DELETE FROM Events " + \
               "WHERE id = " + f"'{event_id}'" + ";")


@app.delete("/events")
async def delete_all_events():
    db.execute("DELETE FROM Events")


@app.post("/events/{event.id}")
async def create_event(event:Event):
    return new_event(event)


@app.put("/events/{event.id}")
async def update_event(event: Event) -> Event:
    return change_event(event)