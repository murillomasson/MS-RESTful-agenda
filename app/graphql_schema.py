import enum
import strawberry
from typing import List
from database import db
import models


@strawberry.enum
class GQLPhoneType(enum.Enum):
    mobile = "mobile"
    landline = "landline"
    business = "business"


@strawberry.enum
class GQLContactCategory(enum.Enum):
    personal = "personal"
    family = "family"
    business = "business"


@strawberry.type
class Phone:
    id: int
    number: str
    type: GQLPhoneType


@strawberry.type
class Contact:
    id: int
    name: str
    category: GQLContactCategory
    phones: List[Phone]


@strawberry.type
class Query:
    @strawberry.field
    def list_contacts(self) -> List[Contact]:
        session = db.get_session()
        contacts = session.query(models.Contact).all()
        return contacts

    @strawberry.field
    def get_contact(self, contact_id: int) -> Contact | None:
        session = db.get_session()
        return session.query(models.Contact).filter(models.Contact.id == contact_id).first()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_contact(
        self,
        name: str,
        category: GQLContactCategory,
        phones: List[str]
    ) -> Contact:
        session = db.get_session()
        contact = models.Contact(name=name, category=category.value)
        session.add(contact)
        session.flush()

        for p in phones:
            tipo, numero = p.split(":")
            phone = models.Phone(number=numero, type=tipo, contact_id=contact.id)
            session.add(phone)

        session.commit()
        session.refresh(contact)
        return contact
