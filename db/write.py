import logging

from sqlalchemy import select
from sqlalchemy.orm import Session

from db import database
from db.models.base_template import MySocialLink
from db.models.main_page import MainTable, FollowMeText
from db.read import GetQuote, GetInfoFooter




class WriteQuote:
    # Возможно поменять название методов и класса чтоб совпадало с таблоицей
    @staticmethod
    def edit_quote(text: str):
        session = database.create_session()
        with session() as session_db:
            stmt = select(MainTable)
            res = session_db.scalars(stmt).first()
            res: MainTable
            res.text = text
            session_db.commit()


class WriteInfoFooter:
    @staticmethod
    def edit_info_footer(text: str):
        print("СОхраняем новую цитату follow me")
        session = database.create_session()
        with session() as session_db:
            stmt = select(FollowMeText).limit(1)
            data_footer = session_db.scalars(stmt).first()
            data_footer: FollowMeText
            data_footer.text = text
            session_db.commit()

    @staticmethod
    def edit_link_footer(link):
        print("СОхраняем новую цитату follow me")
        session = database.create_session()
        with session() as session_db:
            stmt = select(FollowMeText).limit(1)
            data_footer = session_db.scalars(stmt).first()
            data_footer: FollowMeText
            data_footer.link = link
            session_db.commit()


class WriteLinkSocial:
    @staticmethod
    def edit_telegram(new_telegram):
        session = database.create_session()
        with session() as session_db:
            stmt = select(MySocialLink).limit(1)
            data_footer = session_db.scalars(stmt).first()
            data_footer: MySocialLink
            data_footer.telegram = new_telegram
            session_db.commit()

    @staticmethod
    def edit_instagram(new_instagram):
        session = database.create_session()
        with session() as session_db:
            stmt = select(MySocialLink).limit(1)
            data_footer = session_db.scalars(stmt).first()
            data_footer: MySocialLink
            data_footer.instagram = new_instagram
            session_db.commit()
