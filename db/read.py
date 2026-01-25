from sqlalchemy import select

from db import database
from db.models.base_template import MySocialLink
from db.models.contact_page_table import PreviewText, ContactInfo
from db.models.main_page import MainTable, FollowMeText
from db.models.price_page_db import Service, InfoService, BeforeWork, MyCondition, ConditionVideo, AdditionalInfo, \
    Discount, OrderPhotoShootText
from db.models.review_page_table import Reviews


class GetQuote:
    @staticmethod
    def get_text_quote() -> str:
        session = database.create_session()
        with session() as session_db:
            stmt = select(MainTable).limit(1)
            res: MainTable = session_db.scalars(stmt).one_or_none()
            if res is None:
                return "Цитата"
            text = res.text
        return text


class GetInfoFooter:
    @staticmethod
    def get_info() -> str:
        session = database.create_session()
        with session() as session_db:
            stmt = select(FollowMeText).limit(1)
            res: FollowMeText = session_db.scalars(stmt).one_or_none()
        if res is None:
            return "Приглашение в соц. сеть"
        return res.text

    @staticmethod
    def get_link() -> str:
        session = database.create_session()
        with session() as session_db:
            stmt = select(FollowMeText).limit(1)
            res: FollowMeText = session_db.scalars(stmt).first()
        if res is None or "":
            return "Тестовые данные"
        return res.link


class GetSocialLink:
    @staticmethod
    def telegram_link() -> str:
        session = database.create_session()
        with session() as session_db:
            stmt = select(MySocialLink).limit(1)
            res: MySocialLink = session_db.scalars(stmt).one_or_none()
        if res is None:
            return "Ссылка на тг"
        return res.telegram

    @staticmethod
    def instagram_link() -> str:
        session = database.create_session()
        with session() as session_db:
            stmt = select(MySocialLink).limit(1)
            res: MySocialLink = session_db.scalars(stmt).one_or_none()
        if res is None:
            return "Ссылка на инсту"
        return res.instagram


class GetServices:
    @staticmethod
    def all_services():
        session = database.create_session()
        with session() as session_db:
            res = session_db.scalars(select(Service)).all()
        return res


class GetStages:
    @staticmethod
    def all():
        session = database.create_session()
        with session() as session_db:
            res = session_db.scalars(select(BeforeWork).order_by(BeforeWork.id)).all()
        return res


class GetMyConditions:
    @staticmethod
    def all():
        session = database.create_session()
        with session() as session_db:
            res = session_db.scalars(select(MyCondition)).all()
        return res


class GetConditionVideo:
    @staticmethod
    def get():
        session = database.create_session()
        with session() as session_db:
            res = session_db.scalars(select(ConditionVideo)).first()
        return res


class GetAdditionalInfo:
    @staticmethod
    def all():
        session = database.create_session()
        with session() as session_db:
            res = session_db.scalars(select(AdditionalInfo)).all()
        return res


class GetDiscountInfo:
    @staticmethod
    def all():
        session = database.create_session()
        with session() as session_db:
            res = session_db.scalars(select(Discount)).all()
        return res


class OrderPhotoShootTextDB:
    @staticmethod
    def get():
        session = database.create_session()
        with session() as session_db:
            res = session_db.scalar(select(OrderPhotoShootText))
        return res


class PreviewTextContactPage:
    @staticmethod
    def get():
        session = database.create_session()
        with session() as session_db:
            res = session_db.scalar(select(PreviewText))
        return res


class ContactMeInfoContactPage:
    @staticmethod
    def get():
        session = database.create_session()
        with session() as session_db:
            res = session_db.scalar(select(ContactInfo))
        return res


class ReviewsPage:
    @staticmethod
    def get_reviews():
        session = database.create_session()
        with session() as session_db:
            # order by - date
            res = session_db.scalars(select(Reviews).filter_by(active=True)).all()
        return res

    @staticmethod
    def get_inactive_reviews():
        session = database.create_session()
        with session() as session_db:
            # order by - date
            res = session_db.scalars(select(Reviews).filter_by(active=False)).all()
        return res
