import json
import os

from flask import render_template, jsonify, request
from werkzeug.datastructures import FileStorage

from config import PathImg
from db.read import GetQuote, GetInfoFooter, GetSocialLink, ReviewsPage, PreviewTextContactPage, \
    ContactMeInfoContactPage
from db.write import Review


def main_page():
    ImagesPath = PathImg()
    path_big_img, _, _ = ImagesPath.PhotosMainPage()
    big_images: list = os.listdir(path_big_img)
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
    path = PathImg.BackgroundPricePage()
    bg_image = os.listdir(path)[0]
    return render_template(
        "price.html",
        bg_image=bg_image
    )


def review_page():
    reviews = ReviewsPage.get_reviews()
    if len(reviews) == 0:
        reviews = False
    return render_template(
        "reviews.html",
        reviews=reviews
    )


def add_new_review():
    photo_review = request.files.get("photo")
    data = request.form.get("data")
    review = json.loads(data)
    Review.add_new_review(data_review=review, photo_review_title=photo_review)
    return jsonify({"status": True}), 200


def contacts_page():
    ImagesPath = PathImg()
    preview_text = PreviewTextContactPage().get()
    contact_me_info = ContactMeInfoContactPage().get()
    avatar_title: str = os.listdir(ImagesPath.Link())[0]
    telegram_link, instagram_link = GetSocialLink.telegram_link(), GetSocialLink.instagram_link()
    return render_template(
        "contacts.html",
        preview_text=preview_text.text,
        contact_me_info_title=contact_me_info.title,
        contact_me_info_text=contact_me_info.text,
        contact_me_info_number=contact_me_info.number,
        avatar_title=avatar_title,
        telegram=telegram_link,
        instagram=instagram_link
    )