from fastapi import Depends
from sqlmodel import create_engine, Session
from typing import Annotated

engine = create_engine("sqlite:///database.db")

def get_session():
    with Session(engine) as session:
        yield session

GetSession = Annotated[Session, Depends(get_session)]
