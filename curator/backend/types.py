from pydantic import BaseModel


class NewsRequestInput(BaseModel):
    email: str
    mode: str  # {'uplifting', 'neutral', 'demoralizing'}
    tone: str  # {'simple', 'casual', 'academic'}
    length: str  # {'short', 'original'}
