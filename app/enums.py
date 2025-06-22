from enum import Enum


class PhoneType(str, Enum):
    MOBILE = "mobile"
    LANDLINE = "landline"
    BUSINESS = "business"


class ContactCategory(str, Enum):
    FAMILY = "family"
    PERSONAL = "personal"
    BUSINESS = "business"
