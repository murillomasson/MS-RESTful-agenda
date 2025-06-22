from sqlalchemy.orm import Session
import models
import schema


def create_contact(db: Session, contact_data: schema.ContactCreate):
    contact = models.Contact(
        name=contact_data.name,
        category=contact_data.category
    )
    db.add(contact)
    db.flush()

    for phone_data in contact_data.phones:
        phone = models.Phone(
            number=phone_data.number,
            type=phone_data.type,
            contact_id=contact.id
        )
        db.add(phone)

    db.commit()
    db.refresh(contact)
    return contact


def get_contact(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()


def list_contacts(db: Session):
    return db.query(models.Contact).all()
