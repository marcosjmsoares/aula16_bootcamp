from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine
from sqlalchemy import text

engine = create_engine("sqlite:///database.db", echo=True)

with Session(engine) as session:
    statement = text("select * from hero;")

    results = session.exec(statement)

    heroes = results.fetchall()

    for hero in heroes:
        print(hero)    