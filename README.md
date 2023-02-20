# Kafka Project
To run project clone it on your local device and run

```bash
docker compose up
```

Docker compose consists of 9 services:
1. Kafka - 2 topics with 3 partitions - events.taxonomy, bets.state
2. Zookeeper - Kafka metadata
3. PostgreSQL - database
4. Admin page for PostgreSQL - UI service
5. API for Users and Bets - CRUDs for tables Users and Bets
6. API for events - CRUDs for table Events
7. Consumer BetWriter - read message from bets.state and write changes in table Bets
8. Consumer BetScorer - change state of a bet according to changes in Event and send message to topic bets.state 
9. Consumer EventWriter - reads message from topic events.taxonomy and write it to Events
