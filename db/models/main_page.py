from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.models import Base


class MainTable(Base):
    __tablename__ = "preview_text_main_page"
    text: Mapped[str] = mapped_column(String)


class FollowMeText(Base):
    __tablename__ = "follow_me_main_page"
    text: Mapped[str] = mapped_column(String)
    link: Mapped[str] = mapped_column(String)