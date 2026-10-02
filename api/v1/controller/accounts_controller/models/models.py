from sqlmodel import Field, SQLModel


# Base model class - shared fields for all representations of a room
class AccountBase(SQLModel):
    email: str = Field()
    password: int = Field()
    


# Account table model - maps to the "accounts" database table
class Account(AccountBase, table=True):
    __tablename__: str = "accounts"

    id: int | None = Field(default=None, primary_key=True)


# Account response model - the payload to send back to the client
# Guaranteed to have ID for the account (account must exist)
class AccountPublic(AccountBase):
    id: int


# Account update model - all fields can be optional becaue
# we fallback to None
class AccountUpdate(SQLModel):
    email: str | None = None
    password: int | None = None
