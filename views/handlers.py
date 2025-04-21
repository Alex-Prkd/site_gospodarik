import os

from flask import render_template


def main_page():
    names_img: list = os.listdir("static/img/photos")
    return render_template('index.html',
                           images=names_img
                           )