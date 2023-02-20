from pydantic import BaseModel, validator


class Bet(BaseModel):
    id: int
    date: str = '2022-12-03'
    user_id: str
    event_id: int
    market: str

    @validator('date')
    def check_a_date(cls, value):
        from datetime import datetime
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return value

    @validator('market')
    def check_market(cls, value):
        if value not in ['team_1', 'team_2', 'draw']:
            raise ValueError("Market should be in ['team_1', 'team_2', 'draw']")
        else:
            return value




