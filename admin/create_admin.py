from flask import Flask

from admin.admin_handlers import admin_main_page, admin_price_page, admin_review_page, admin_contacts_page
from admin.main_views import remove_photo_view, edit_avatar_photo, add_new_photo
from admin.price_views import remove_service, edit_before_work


def admin_main_views(app: Flask):
    app.add_url_rule("/admin/add_new_photo/", methods=["POST"], view_func=add_new_photo)
    app.add_url_rule("/admin/remove_photo_main_page/", methods=["POST"], view_func=remove_photo_view)
    app.add_url_rule("/admin/edit_avatar_photo/", methods=["POST"], view_func=edit_avatar_photo)


def price_views(app: Flask):
    app.add_url_rule("/admin/remove_services", methods=["POST"], view_func=remove_service)
    app.add_url_rule("/admin/edit_before_work", methods=["POST"], view_func=edit_before_work)


def admin_pages(app: Flask):
    app.add_url_rule("/admin/", methods=["GET", "POST"], view_func=admin_main_page)
    admin_main_views(app)

    app.add_url_rule("/admin/price", methods=["GET", "POST"], view_func=admin_price_page)
    price_views(app)
    app.add_url_rule("/admin/reviews", methods=["GET", "POST"], view_func=admin_review_page)
    app.add_url_rule("/admin/contacts", methods=["GET", "POST"], view_func=admin_contacts_page)
