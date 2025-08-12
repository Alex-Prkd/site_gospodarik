from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from db.models import Base

from db.models.base_template import MySocialLink
from db.models.contact_page_table import PreviewText, ContactInfo

from db.models.main_page import MainTable
from db.models.price_page_db import Discount, AdditionalInfo, InfoService, Service, MyCondition, ConditionVideo, \
    Information, BeforeWork
from db.models.review_page_table import Reviews


class CreateEngineSession:
    def __init__(self):
        self.engine = create_engine("sqlite:///db/information.db")
        self.base: DeclarativeBase = Base()

    def create_session(self) -> sessionmaker:
        session = sessionmaker(bind=self.engine)
        return session

    def create_db_and_tables(self) -> None:
        self.base.metadata.create_all(bind=self.engine)