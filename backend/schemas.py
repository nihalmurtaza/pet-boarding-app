from pydantic import BaseModel, EmailStr

# User Schema
class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str = None
    disabled: bool = False

# Pet Schema
class Pet(BaseModel):
    id: int
    owner_id: int
    name: str
    species: str
    breed: str = None
    age: int = None

# Booking Schema
class Booking(BaseModel):
    id: int
    pet_id: int
    start_date: str
    end_date: str
    status: str
