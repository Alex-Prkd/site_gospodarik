from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from db.models import Base


class PreviewText(Base):
    __tablename__ = "preview text"
    text: Mapped[str] = mapped_column(String())


class ContactInfo(Base):
    __tablename__ = "contact info"
    text: Mapped[str] = mapped_column(String())