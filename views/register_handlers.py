from flask import Flask

from views.handlers import main_page


def pages(app: Flask):
    app.add_url_rule("/", methods=["GET", "POST"], view_func=main_page)