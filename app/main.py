from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import db, Base
from schema import ContactCreate, ContactRead
from graphql_schema import Query, Mutation
import strawberry
from strawberry.fastapi import GraphQLRouter
import crud


app = FastAPI()
Base.metadata.create_all(bind=db.engine)


def get_db():
    session = db.get_session()
    try:
        yield session
    finally:
        session.close()


@app.get("/", tags=["Healthcheck"])
def read_root():
    return {"message": "Hi there :) API is running"}


@app.post("/contacts/", response_model=ContactRead, tags=["Contacts"])
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, contact)


@app.get("/contacts/{contact_id}", response_model=ContactRead, tags=["Contacts"])
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = crud.get_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact


@app.get("/contacts/", response_model=list[ContactRead], tags=["Contacts"])
def list_all_contacts(db: Session = Depends(get_db)):
    return crud.list_contacts(db)


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")