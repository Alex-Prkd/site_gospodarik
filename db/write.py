import os

from typing import List, Union

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.datastructures import FileStorage

from admin.WorkWithImgServices.ConvertSizeIMG import CreateCopySmallSizeIMG
from config import PathImg
from db import database
from db.models.base_template import MySocialLink
from db.models.contact_page_table import PreviewText, ContactInfo
from db.models.main_page import MainTable, FollowMeText
from db.models.price_page_db import Service, InfoService, BeforeWork, Information, MyCondition, ConditionVideo, \
    AdditionalInfo, Discount, OrderPhotoShootText
from db.models.review_page_table import Reviews


class WriteQuote:
    @staticmethod
    def default_quote():
        session = database.create_session()
        with session() as session_db:
            res = MainTable(text="'Цитата!'")
            session_db.add(res)
            session_db.commit()


    @staticmethod
    def edit_quote(new_quote: str):
        session = database.create_session()
        with session() as session_db:
            stmt = select(MainTable)
            res = session_db.scalars(stmt).first()
            res: MainTable
            res.text = new_quote
            session_db.commit()


class WriteInfoFooter:
    @staticmethod
    def default_info_and_link_footer():
        session = database.create_session()
        with session() as session_db:
            res = FollowMeText(
                text="'Приглашение в instagram:'",
                link="'@Ссылка instagram'"
            )
            session_db.add(res)
            session_db.commit()

    @staticmethod
    def edit_info_footer(new_text: str):
        session = database.create_session()
        with session() as session_db:
            stmt = select(FollowMeText).limit(1)
            data_footer = session_db.scalars(stmt).first()
            data_footer: FollowMeText
            data_footer.text = new_text
            session_db.commit()

    @staticmethod
    def edit_link_footer(link):
        session = database.create_session()
        with session() as session_db:
            stmt = select(FollowMeText).limit(1)
            data_footer = session_db.scalars(stmt).first()
            data_footer: FollowMeText
            data_footer.link = link
            session_db.commit()



class WriteLinkSocial:
    @staticmethod
    def default_link_social():
        session = database.create_session()
        with session() as session_db:
            res = MySocialLink(
                instagram="'https://www.instagram.com/'",
                telegram="'https://web.telegram.org/'"
            )
            session_db.add(res)
            session_db.commit()


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


class WriteNewService:
    @staticmethod
    def add_service(title: str, descriptions: list, img_title: str, price: int):
        session = database.create_session()
        try:
            with session() as session_db:
                service: Service = Service()
                service.title = title
                service.price = price
                service.img = img_title
                info = []
                for description in descriptions:
                    info.append(InfoService(text=description))
                service.info = info
                session_db.add(service)
                session_db.commit()
                return True
        except SQLAlchemyError:
            session_db.rollback()
            return False


class RemoveServiceDB:
    @staticmethod
    def remove(id: str):
        session = database.create_session()
        with session() as session_db:
            service: Service = session_db.get(Service, id)
            session_db.delete(service)
            session_db.commit()
        return service.img


class EditService:
    @staticmethod
    def edit_img_service(old_img: str, new_img: str):
        session = database.create_session()
        try:
            with session() as session_db:
                stmt = select(Service).where(Service.img == old_img)
                service: Service = session_db.scalar(stmt)
                service.img = new_img
                session_db.add(service)
                session_db.commit()
            return True
        except Exception:
            return False

    @staticmethod
    def edit_title(service_id: int, new_title: str):
        session = database.create_session()
        with session() as session_db:
            service: Service = session_db.get(Service, service_id)
            service.title = new_title
            session_db.add(service)
            session_db.commit()

    @staticmethod
    def edit_description(description_id: int, new_description: str):
        session = database.create_session()
        with session() as session_db:
            description: InfoService = session_db.get(InfoService, description_id)
            description.text = new_description
            session_db.add(description)
            session_db.commit()

    @staticmethod
    def edit_price(service_id: int, new_price: float):
        session = database.create_session()
        with session() as session_db:
            service: Service = session_db.get(Service, service_id)
            service.price = new_price
            session_db.add(service)
            session_db.commit()


    @staticmethod
    def add_description(service_id: int, text: str):
        session = database.create_session()
        with session() as session_db:
            service: Service = session_db.get(Service, service_id)
            description: InfoService = InfoService(
                text=text,
                service=service
            )
            session_db.add(description)
            session_db.commit()
            return description.id

    @staticmethod
    def remove_descriptions(descriptions_id: List):
        session = database.create_session()
        with session() as session_db:
            for id in descriptions_id:
                description = session_db.get(InfoService, id)
                session_db.delete(description)
                session_db.commit()


class EditStageWorkDB:
    @staticmethod
    def new_stage_work(title: str, conditions: List):
        session = database.create_session()
        with session() as session_db:
            new_stage: BeforeWork = BeforeWork()
            all_conditions = [Information(text=condition) for condition in conditions]
            new_stage.title = title
            new_stage.info_to_work = all_conditions
            session_db.add(new_stage)
            session_db.commit()

    @staticmethod
    def edit_title(values):
        id, title = values.values()
        session = database.create_session()
        with session() as session_db:
            stage: BeforeWork = session_db.get(BeforeWork, id)
            stage.title = title
            session_db.add(stage)
            session_db.commit()

    @staticmethod
    def edit_conditions(values: list):
        conditions = []
        session = database.create_session()
        with session() as session_db:
            for dict_condition in values:
                id, new_text = dict_condition.values()
                condition: Information = session_db.get(Information, id)
                condition.text = new_text
                conditions.append(condition)
            session_db.add_all(conditions)
            session_db.commit()

    @staticmethod
    def remove_condition(id):
        session = database.create_session()
        with session() as session_db:
            condition = session_db.get(Information, id)
            session_db.delete(condition)
            session_db.commit()

    @staticmethod
    def new_condition(stage_id, text):
        session = database.create_session()
        with session() as session_db:
            condition: Information = Information()
            condition.text = text
            condition.work_id = stage_id
            session_db.add(condition)
            session_db.commit()

    @staticmethod
    def remove_stage(stage_id):
        session = database.create_session()
        with session() as session_db:
            stage = session_db.get(BeforeWork, stage_id)
            session_db.delete(stage)
            session_db.commit()


class MyConditionDB:
    @staticmethod
    def create(text: str):
        session = database.create_session()
        with session() as session_db:
            condition = MyCondition(text=text)
            session_db.add(condition)
            session_db.commit()

    @staticmethod
    def edit(id, text):
        session = database.create_session()
        with session() as session_db:
            condition: MyCondition = session_db.get(MyCondition, id)
            condition.text = text
            session_db.add(condition)
            session_db.commit()

    @staticmethod
    def remove(id):
        session = database.create_session()
        with session() as session_db:
            condition: MyCondition = session_db.get(MyCondition, id)
            session_db.delete(condition)
            session_db.commit()


class ConditionVideoDB:
    @staticmethod
    def create_default_condition_video():
        session = database.create_session()
        with session() as session_db:
            res = ConditionVideo(text="Пустое поле.")
            session_db.add(res)
            session_db.commit()

    @staticmethod
    def edit(id, new_text: str):
        session = database.create_session()
        with session() as session_db:
            condition_video: ConditionVideo = session_db.get(ConditionVideo, id)
            condition_video.text = new_text
            session_db.add(condition_video)
            session_db.commit()


class AdditionalInfoDB:
    @staticmethod
    def edit(id, new_text: str):
        session = database.create_session()
        with session() as session_db:
            information: AdditionalInfo = session_db.get(AdditionalInfo, id)
            information.text = new_text
            session_db.add(information)
            session_db.commit()

    @staticmethod
    def remove(id):
        session = database.create_session()
        with session() as session_db:
            information: AdditionalInfo = session_db.get(AdditionalInfo, id)
            session_db.delete(information)
            session_db.commit()

    @staticmethod
    def create(text: str):
        session = database.create_session()
        with session() as session_db:
            information = AdditionalInfo(text=text)
            session_db.add(information)
            session_db.commit()


class DiscountDB:
    @staticmethod
    def create(text: str):
        session = database.create_session()
        with session() as session_db:
            new_discount = Discount(text=text)
            session_db.add(new_discount)
            session_db.commit()

    @staticmethod
    def edit(id, new_text: str):
        session = database.create_session()
        with session() as session_db:
            discount: Discount = session_db.get(Discount, id)
            discount.text = new_text
            session_db.add(discount)
            session_db.commit()

    @staticmethod
    def remove(id):
        session = database.create_session()
        with session() as session_db:
            discount = session_db.get(Discount, id)
            session_db.delete(discount)
            session_db.commit()


class OrderPhotoShootDB:
    @staticmethod
    def create_default_condition_video():
        session = database.create_session()
        with session() as session_db:
            res = OrderPhotoShootText(text="Пустое поле.")
            session_db.add(res)
            session_db.commit()

    @staticmethod
    def edit(new_text):
        session = database.create_session()
        with session() as session_db:
            order_photo_shoot_text = session_db.scalar(select(OrderPhotoShootText))
            order_photo_shoot_text.text = new_text
            session_db.add(order_photo_shoot_text)
            session_db.commit()


class PreviewTextContactPageDB:
    @staticmethod
    def create_default_text():
        session = database.create_session()
        with session() as session_db:
            res = PreviewText(text="Пустое поле.")
            session_db.add(res)
            session_db.commit()

    @staticmethod
    def edit_text(new_text: str):
        session = database.create_session()
        with session() as session_db:
            preview = session_db.scalar(select(PreviewText))
            preview.text = new_text
            session_db.add(preview)
            session_db.commit()


class TextContactMeContactPageDB:
    @staticmethod
    def create_default_tex():
        session = database.create_session()
        with session() as session_db:
            res = ContactInfo(title="Пустое поле.",
                              text="Пустое поле.",
                              number="0")
            session_db.add(res)
            session_db.commit()

    @staticmethod
    def edit_title_text(new_title: str):
        session = database.create_session()
        with session() as session_db:
            contact_info = session_db.scalar(select(ContactInfo))
            contact_info.title = new_title
            session_db.add(contact_info)
            session_db.commit()

    @staticmethod
    def edit_info(new_text: str):
        session = database.create_session()
        with session() as session_db:
            contact_info = session_db.scalar(select(ContactInfo))
            contact_info.text = new_text
            session_db.add(contact_info)
            session_db.commit()

    @staticmethod
    def edit_number(new_number):
        session = database.create_session()
        with session() as session_db:
            contact_info = session_db.scalar(select(ContactInfo))
            contact_info.number = new_number
            session_db.add(contact_info)
            session_db.commit()


class Review:
    @staticmethod
    def accept_inactive_review(id):
        session = database.create_session()
        with session() as session_db:
            inactive_review: Reviews = session_db.scalar(select(Reviews).where(Reviews.id == id))
            inactive_review.active = True
            session_db.add(inactive_review)
            session_db.commit()

    @staticmethod
    def remove_review(id):
        session = database.create_session()
        with session() as session_db:
            review: Reviews = session_db.scalar(select(Reviews).where(Reviews.id == id))
            session_db.delete(review)
            session_db.commit()

    @staticmethod
    def add_new_review(data_review: dict, photo_review_title: Union[FileStorage, None]):
        session = database.create_session()
        with session() as session_db:
            try:
                new_review = Reviews()
                if photo_review_title is not None:
                    new_review.photo = photo_review_title.filename
                new_review.nickname = data_review["name"]
                new_review.review_text = data_review["review"]
                new_review.social_link = data_review["social_link"]
                session_db.add(new_review)
                session_db.commit()
                if photo_review_title is not None:
                    path_big_img, path_middle_img, path_small_img = PathImg.AddNewReviewPhoto()
                    photo_review_title.save(os.path.join(path_big_img, photo_review_title.filename))
                    CreateCopySmallSizeIMG().createMobileIMG(
                        name_img=photo_review_title.filename,
                        path_big_img=path_big_img,
                        path_middle_img=path_middle_img,
                        path_small_img=path_small_img
                    )
            except SQLAlchemyError:
                session_db.rollback()
            except Exception:
                "Логгирование ошибки"
                pass