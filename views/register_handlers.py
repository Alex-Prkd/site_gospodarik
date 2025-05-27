from flask import Flask

from views.handlers import main_page, price_page, review_page, contacts_page


def pages(app: Flask):
    app.add_url_rule("/", methods=["GET", "POST"], view_func=main_page)
    app.add_url_rule("/price", methods=["GET", "POST"], view_func=price_page)
    app.add_url_rule("/reviews", methods=["GET", "POST"], view_func=review_page)
    app.add_url_rule("/contacts", methods=["GET", "POST"], view_func=contacts_page)
