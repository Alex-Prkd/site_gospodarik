from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.models import Base


class Reviews(Base):
    __tablename__ = "reviews"
    photo: Mapped[str] = mapped_column(String())
    nickname: Mapped[str] = mapped_column(String())
    review_text: Mapped[str] = mapped_column(String(300))