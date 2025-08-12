import os

from flask import render_template

from db.read import GetQuote, GetInfoFooter, GetSocialLink


def main_page():
    names_img: list = os.listdir("static/img/photos")
    avatar_img: str = os.listdir(os.path.abspath("static/img/link"))[0]
    quote = GetQuote().get_text_quote()
    text_footer, link_footer = GetInfoFooter.get_info(), GetInfoFooter.get_link()
    instagram, telegram = GetSocialLink.instagram_link(), GetSocialLink.telegram_link()
    return render_template(
        'main.html',
        images=names_img,
        avatar=avatar_img,
        quote=quote,
        text_footer=text_footer,
        link_footer=link_footer,
        instagram=instagram,
        telegram=telegram
    )


def price_page():
    return render_template(
        "price.html"
    )


def review_page():
    return render_template(
        "reviews.html"
    )


def contacts_page():
    return render_template(
        "contacts.html"
    )