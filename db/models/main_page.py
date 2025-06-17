from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.models import Base


class MainTable(Base):
    __tablename__ = "preview_text"
    text: Mapped[str] = mapped_column(String)