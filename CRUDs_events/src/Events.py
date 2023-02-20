from pydantic import BaseModel, validator


class Event(BaseModel):
    id: int
    type: str
    team_1: str
    team_2: str
    event_date: str = '2022-12-03'
    score: str = '0-0'
    state: str = 'created'

    @validator('event_date')
    def check_a_date(cls, value):
        from datetime import datetime
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return value

    @validator('score')
    def check_score(cls, value):
        import regex as re
        if re.fullmatch(r'\d+-\d+', value):
            return value
        else:
            raise ValueError('Score does not match format "int-int"')

    @validator('state')
    def check_state(cls, value):
        if value not in ['created', 'active', 'finished']:
            raise ValueError("State should be in ['created', 'active', 'finished']")
        else:
            return value
