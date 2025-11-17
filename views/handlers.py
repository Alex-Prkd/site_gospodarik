import os

from flask import render_template
from config import PathImg
from db.read import GetQuote, GetInfoFooter, GetSocialLink



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
    return render_template(
        "reviews.html"
    )


def contacts_page():
    return render_template(
        "contacts.html"
    )