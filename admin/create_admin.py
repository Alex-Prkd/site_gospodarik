from flask import Flask

from admin.admin_handlers import admin_main_page, admin_price_page, admin_review_page, admin_contacts_page
from admin.contact_page_views import save_preview_text
from admin.main_views import remove_photo_view, edit_avatar_photo, add_new_photo, edit_quote, edit_follow_me_text, \
    edit_follow_me_link, edit_link_telegram, edit_link_instagram
from admin.price_views import remove_service, add_service, edit_img_service, edit_title_service, \
    edit_description_service, edit_price_service, add_new_description_service, remove_descriptions_service, \
    create_new_stage_work, edit_stage, remove_condition, new_condition_stage, remove_stage, add_new_my_condition, \
    change_my_condition, remove_my_condition, change_condition_video, edit_background_photo_price_page, \
    edit_info_footer, remove_info_footer, add_new_info_footer, edit_discount, remove_discount, add_new_discount, \
    edit_order_text


def admin_main_views(app: Flask):
    app.add_url_rule("/admin/add_new_photo/", methods=["POST"], view_func=add_new_photo)
    app.add_url_rule("/admin/remove_photo_main_page/", methods=["POST"], view_func=remove_photo_view)
    app.add_url_rule("/admin/edit_avatar_photo/", methods=["POST"], view_func=edit_avatar_photo)
    app.add_url_rule("/admin/edit_quote", methods=["POST"], view_func=edit_quote)
    app.add_url_rule("/admin/edit_follow_me_text", methods=["POST"], view_func=edit_follow_me_text)
    app.add_url_rule("/admin/edit_follow_me_link", methods=["POST"], view_func=edit_follow_me_link)
    app.add_url_rule("/admin/edit_telegram_link", methods=["POST"], view_func=edit_link_telegram)
    app.add_url_rule("/admin/edit_instagram_link", methods=["POST"], view_func=edit_link_instagram)



def price_views(app: Flask):
    app.add_url_rule("/admin/new_service", methods=["POST"], view_func=add_service)
    app.add_url_rule("/admin/edit_photo_service", methods=["POST"], view_func=edit_img_service)
    app.add_url_rule("/admin/edit_title_service", methods=["POST"], view_func=edit_title_service)
    app.add_url_rule("/admin/edit_info_service", methods=["POST"], view_func=edit_description_service)
    app.add_url_rule("/admin/edit_price_service", methods=["POST"], view_func=edit_price_service)
    app.add_url_rule("/admin/add_new_description", methods=["POST"], view_func=add_new_description_service)
    app.add_url_rule("/admin/remove_descriptions", methods=["POST"], view_func=remove_descriptions_service)
    app.add_url_rule("/admin/remove_services", methods=["POST"], view_func=remove_service)
    app.add_url_rule("/admin/remove_condition", methods=["POST"], view_func=remove_condition)
    app.add_url_rule("/admin/create_new_stage_work", methods=["POST"], view_func=create_new_stage_work)
    app.add_url_rule("/admin/edit_stage", methods=["POST"], view_func=edit_stage)
    app.add_url_rule("/admin/add_new_condition_stage", methods=["POST"], view_func=new_condition_stage)
    app.add_url_rule("/admin/remove_stage", methods=["POST"], view_func=remove_stage)
    app.add_url_rule("/admin/create_my_condition", methods=["POST"], view_func=add_new_my_condition)
    app.add_url_rule("/admin/change_my_condition", methods=["POST"], view_func=change_my_condition)
    app.add_url_rule("/admin/remove_my_condition", methods=["POST"], view_func=remove_my_condition)
    app.add_url_rule("/admin/change_condition_video", methods=["POST"], view_func=change_condition_video)
    app.add_url_rule("/admin/edit_photo_background_price_page", methods=["POST"], view_func=edit_background_photo_price_page)
    app.add_url_rule("/admin/edit_info_footer", methods=["POST"], view_func=edit_info_footer)
    app.add_url_rule("/admin/remove_info_footer", methods=["POST"], view_func=remove_info_footer)
    app.add_url_rule("/admin/add_new_info_footer", methods=["POST"], view_func=add_new_info_footer)
    app.add_url_rule("/admin/edit_discount", methods=["POST"], view_func=edit_discount)
    app.add_url_rule("/admin/remove_discount", methods=["POST"], view_func=remove_discount)
    app.add_url_rule("/admin/add_new_discount", methods=["POST"], view_func=add_new_discount)
    app.add_url_rule("/admin/edit_order_text", methods=["POST"], view_func=edit_order_text)


def contact_views(app: Flask):
    app.add_url_rule("/admin/edit_preview_contact_page", methods=["POST"], view_func=save_preview_text)


def admin_pages(app: Flask):
    app.add_url_rule("/admin/", methods=["GET", "POST"], view_func=admin_main_page)
    admin_main_views(app)

    app.add_url_rule("/admin/price", methods=["GET", "POST"], view_func=admin_price_page)
    price_views(app)
    app.add_url_rule("/admin/reviews", methods=["GET", "POST"], view_func=admin_review_page)
    app.add_url_rule("/admin/contacts", methods=["GET", "POST"], view_func=admin_contacts_page)
    contact_views(app)
