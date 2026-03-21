import json
import os

from flask import render_template, jsonify, request
from werkzeug.datastructures import FileStorage

from admin.WorkWithImgServices.ConvertSizeIMG import CreateCopySmallSizeIMG
from config import PathImg
from db.models.price_page_db import Service
from db.read import GetQuote, GetInfoFooter, GetSocialLink, ReviewsPage, PreviewTextContactPage, \
    ContactMeInfoContactPage, GetServices, GetStages, GetMyConditions, GetConditionVideo, GetAdditionalInfo, \
    GetDiscountInfo, OrderPhotoShootTextDB
from db.write import Review


def main_page():
    ImagesPath = PathImg()
    path_big_img, _, _ = ImagesPath.PhotosMainPage()
    big_images: list = sorted(
        os.listdir(path_big_img),
        key=lambda image: os.path.getctime(os.path.join(path_big_img, image)),
        reverse=True
    )
    avatar_img = os.listdir(ImagesPath.Link())[0]
    quote = GetQuote().get_text_quote()
    text_footer, link_footer = GetInfoFooter.get_info(), GetInfoFooter.get_link()
    instagram, telegram = GetSocialLink.instagram_link(), GetSocialLink.telegram_link()
    return render_template(
        'main.html',
        images=big_images,
        avatar=avatar_img,
        quote=quote,
        text_footer=text_footer,
        link_footer=link_footer,
        instagram=instagram,
        telegram=telegram
    )


def price_page():
    path = PathImg()
    avatar_img = os.listdir(path.Link())[0]
    bg_image = os.listdir(path.BackgroundPricePage())[0]
    services = GetServices().all_services()
    stages = GetStages().all()
    my_condition = GetMyConditions().all()
    condition_video = GetConditionVideo().get()
    additional_info = GetAdditionalInfo.all()
    discount_info = GetDiscountInfo.all()
    order_photo_shoot_info = OrderPhotoShootTextDB.get()
    instagram, telegram = GetSocialLink.instagram_link(), GetSocialLink.telegram_link()
    return render_template(
        "price.html",
        bg_image=bg_image,
        avatar=avatar_img,
        services=services,
        stages=stages,
        my_conditions=my_condition,
        condition_video=condition_video,
        additional_info=additional_info,
        discount_info=discount_info,
        order_photo_shoot_info=order_photo_shoot_info,
        instagram=instagram,
        telegram=telegram
    )


def review_page():
    avatar_img = os.listdir(PathImg().Link())[0]
    reviews = ReviewsPage.get_reviews()
    if len(reviews) == 0:
        reviews = False
    return render_template(
        "reviews.html",
        reviews=reviews,
        avatar=avatar_img
    )


def add_new_review():
    photo_review: FileStorage = request.files.get("photo")
    data = request.form.get("data")
    review = json.loads(data)
    Review.add_new_review(data_review=review, photo_review_title=photo_review)
    return jsonify({"status": True}), 200


def contacts_page():
    ImagesPath = PathImg()
    avatar_img = os.listdir(ImagesPath.Link())[0]
    preview_text = PreviewTextContactPage().get()
    contact_me_info = ContactMeInfoContactPage().get()
    avatar_title: str = os.listdir(ImagesPath.Link())[0]
    telegram_link, instagram_link = GetSocialLink.telegram_link(), GetSocialLink.instagram_link()
    return render_template(
        "contacts.html",
        avatar=avatar_img,
        preview_text=preview_text.text,
        contact_me_info_title=contact_me_info.title,
        contact_me_info_text=contact_me_info.text,
        contact_me_info_number=contact_me_info.number,
        avatar_title=avatar_title,
        telegram=telegram_link,
        instagram=instagram_link
    )