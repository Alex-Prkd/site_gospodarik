from datetime import datetime

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from db.models import Base


class Reviews(Base):
    __tablename__ = "reviews"
    photo: Mapped[str] = mapped_column(String, nullable=True)
    nickname: Mapped[str] = mapped_column(String)
    review_text: Mapped[str] = mapped_column(String(300))
    social_link: Mapped[str] = mapped_column(String, nullable=True)
    active: Mapped[bool] = mapped_column(default=False, unique=False)
    date_added: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    def to_dict(self):
        reviews_dict = {
            "id": self.id,
            "nickname": self.nickname,
            "photo": self.photo,
            "review_text": self.review_text,
            "social_link": self.social_link,
            "active": self.active
        }
        return reviews_dict