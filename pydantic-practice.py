



from pydantic import BaseModel, Field, ValidationError, EmailStr

from typing import List,Dict, Optional, Annotated

#  problem dekhte hai pahle ...

# def insert_data_into_db(name: str, age: int):
#     # Simulating database insertion
#     if isinstance(name, str) and isinstance(age, int):
       
#       print(f"Inserting into database: Name={name}, Age={age}")
#     else:
#       print(f"Error: Invalid data types. Name should be a string and Age should be an integer.")

# # insert_data_into_db("John Doe", 30)  # Example usage

# # insert_data_into_db("Alice", 'twenty five')  # Example usage

# insert_data_into_db("Bob", "25")  # Example usage

# use pydanttic

class User(BaseModel):
    name: Annotated[str, Field(max_length=25, title="name of user", description=' please enter your name within 25 char')]
    age: int = Field(gt=0, lt=70, description="Age must be a positive integer")
    # skills: list  sirf list use krne se list bnata hai but type kuch bhi ho skta hai
    skills: List[str] = Field(..., description="Skills must be a list of strings")
    gender:Optional[str] = None
    email:EmailStr = None


def insert_data_into_db(user: User):
    # Simulating database insertion
    print(f"user: {user}")


# create user
user={
    "name":'farhan',
    "age":60,
    "skills":["Python", "Django", "Flask"],
    # "gender":'Male',
    "location":"delhi",
    "email":"farhanraza2239@gmail.com"
} 


# Example usage
try:
    user = User(**user)
    insert_data_into_db(user)


except ValueError as e:
    print(f"Error: {e}")
