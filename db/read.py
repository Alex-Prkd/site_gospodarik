import logging

from sqlalchemy import select

from db import database
from db.models.base_template import MySocialLink
from db.models.main_page import MainTable, FollowMeText


class GetQuote:
    @staticmethod
    def get_text_quote() -> str:
        print("Получаем текст цитаты")
        session = database.create_session()
        with session() as session_db:
            stmt = select(MainTable).limit(1)
            res: MainTable = session_db.scalars(stmt).one_or_none()
            text = res.text
        return text


class GetInfoFooter:
    @staticmethod
    def get_info() -> str:
        print("Получаем текст инфо")
        session = database.create_session()
        with session() as session_db:
            stmt = select(FollowMeText).limit(1)
            res: FollowMeText = session_db.scalars(stmt).one_or_none()
        if res is None:
            return "Тестовые данные"
        else:
            return res.text

    @staticmethod
    def get_link() -> str:
        print("Получаем текст инфо")
        session = database.create_session()
        with session() as session_db:
            stmt = select(FollowMeText).limit(1)
            res: FollowMeText = session_db.scalars(stmt).first()
        if res is None or "":
            return "Тестовые данные"
        else:
            return res.link


class GetSocialLink:
    @staticmethod
    def telegram_link() -> str:
        print("Получаем текст телеграм")
        session = database.create_session()
        with session() as session_db:
            stmt = select(MySocialLink).limit(1)
            res: MySocialLink = session_db.scalars(stmt).one_or_none()
        if res is None:
            return "Тестовые данные"
        else:
            return res.telegram\


    @staticmethod
    def instagram_link() -> str:
        print("Получаем текст инстаграм")
        session = database.create_session()
        with session() as session_db:
            stmt = select(MySocialLink).limit(1)
            res: MySocialLink = session_db.scalars(stmt).one_or_none()
        if res is None:
            return "Тестовые данные"
        else:
            return res.instagram