import os

from flask import render_template


def main_page():
    names_img: list = os.listdir("static/img/photos")
    return render_template(
        'main.html',
        images=names_img
    )


def price_page():
    return render_template(
        "price.html"
    )


def review_page():
    return render_template(
        "reviews.html"
    )
