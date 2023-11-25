from pydantic import BaseModel


class NewsRequestInput(BaseModel):
    user: str
