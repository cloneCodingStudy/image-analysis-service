from pydantic import BaseModel

class RentalPost(BaseModel):
    title: str
    description: str
    price: int
    condition: str
