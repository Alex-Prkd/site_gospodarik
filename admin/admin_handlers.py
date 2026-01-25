import os

from flask import abort, render_template, request

from config import PathImg
from db.models.price_page_db import BeforeWork
from db.read import GetQuote, GetInfoFooter, GetSocialLink, GetServices, GetStages, GetMyConditions, GetConditionVideo, \
    GetAdditionalInfo, GetDiscountInfo, OrderPhotoShootTextDB, PreviewTextContactPage, ContactMeInfoContactPage, \
    ReviewsPage
from db.write import WriteInfoFooter, WriteQuote, WriteLinkSocial


def admin_main_page():
    ImagesPath = PathImg()
    path_big_img, _, _ = ImagesPath.PhotosMainPage()
    names_img: list = os.listdir(path_big_img)
    avatar_title: str = os.listdir(ImagesPath.Link())[0]
    preview = GetQuote.get_text_quote()
    info_footer = GetInfoFooter.get_info()  # Форма текста под фотографиями
    link_footer = GetInfoFooter.get_link()     # Доп текст с никнеймом в соц. сетях или т.п.
    telegram_link, instagram_link = GetSocialLink.telegram_link(), GetSocialLink.instagram_link()
    return render_template(
        "/admin/main.html",
        telegram_link=telegram_link,
        instagram_link=instagram_link,
        images=names_img,
        preview=preview,
        info_footer=info_footer,
        link_footer=link_footer,
        avatar=avatar_title
    )


def admin_price_page():
    ImagesPath = PathImg()
    avatar_title: str = os.listdir(ImagesPath.Link())[0]
    services = GetServices().all_services()
    stages = GetStages().all()
    conditions = GetMyConditions().all()
    path = os.path.abspath("static/img/background_price_page/")
    bg_image = os.listdir(path)[0]
    condition_video = GetConditionVideo().get()
    additional_info = GetAdditionalInfo.all()
    discount_info = GetDiscountInfo.all()

    text_order_photo_shoot = OrderPhotoShootTextDB.get()

    telegram_link, instagram_link = GetSocialLink.telegram_link(), GetSocialLink.instagram_link()
    return render_template("/admin/price.html",
                           # social=link_social,
                           avatar=avatar_title,
                           conditions=conditions,
                           condition_video=condition_video,
                           services=services,
                           stages=stages,
                           bg_image=bg_image,
                           additional_info=additional_info,
                           discount_info=discount_info,
                           text_order_photo_shoot=text_order_photo_shoot,
                           telegram_link=telegram_link,
                           instagram_link=instagram_link)


def admin_review_page():
    ImagesPath = PathImg()
    avatar_title: str = os.listdir(ImagesPath.Link())[0]
    reviews = ReviewsPage.get_reviews()
    telegram_link, instagram_link = GetSocialLink.telegram_link(), GetSocialLink.instagram_link()
    return render_template("/admin/reviews.html",
                           reviews=reviews,
                           telegram_link=telegram_link,
                           instagram_link=instagram_link,
                           avatar=avatar_title)


def admin_contacts_page():
    ImagesPath = PathImg()
    preview_text = PreviewTextContactPage().get()
    contact_me_info = ContactMeInfoContactPage().get()
    avatar_title: str = os.listdir(ImagesPath.Link())[0]
    telegram_link, instagram_link = GetSocialLink.telegram_link(), GetSocialLink.instagram_link()
    return render_template("/admin/contacts.html",
                           telegram_link=telegram_link,
                           instagram_link=instagram_link,
                           preview_text=preview_text.text,
                           contact_me_info_title=contact_me_info.title,
                           contact_me_info_text=contact_me_info.text,
                           contact_me_info_number=contact_me_info.number,
                           avatar=avatar_title)