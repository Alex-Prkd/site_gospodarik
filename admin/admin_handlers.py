import os

from flask import abort, render_template, redirect, request, flash, jsonify

from admin.forms.main_page import PreviewText, EditInfoFooter, EditLinkSocial, EditLinkFooter
from admin.forms.price_forms import MyConditionForm, ConditionVideoForm
from db.models.price_page_db import BeforeWork
from db.read import GetQuote, GetInfoFooter, GetSocialLink
from db.write import WriteInfoFooter, WriteQuote, WriteLinkSocial


def admin_main_page():
    names_img: list = os.listdir("static/img/photos")
    avatar_title: str = os.listdir("static/img/link")[0]
    preview_form = PreviewText()    # Форма главного текста
    preview_form.text.description = GetQuote.get_text_quote()
    if preview_form.validate_on_submit():
        WriteQuote.edit_quote(preview_form.text.data)
        flash("Запись изменена")
        return redirect("/admin/")

    edit_info_footer = EditInfoFooter()     # Форма текста под фотографиями
    edit_info_footer.follow_me.description = GetInfoFooter.get_info()
    if edit_info_footer.validate_on_submit():
        WriteInfoFooter.edit_info_footer(edit_info_footer.follow_me.data)
        flash("Информация для связи изменена")
        return redirect("/admin/")

    edit_link_footer = EditLinkFooter()     # Доп текст с никнеймом в соц. сетях или т.п.
    edit_link_footer.link.description = GetInfoFooter.get_link()
    if edit_link_footer.validate_on_submit():
        WriteInfoFooter.edit_link_footer(edit_link_footer.link.data)
        flash("Информация для связи изменена")
        return redirect("/admin/")

    link_social = EditLinkSocial()      # Форма ссылки на соц. сети footer страницы
    link_social.telegram.description = GetSocialLink.telegram_link()
    link_social.instagram.description = GetSocialLink.instagram_link()
    if link_social.validate_on_submit():
        if link_social.data["telegram"] != "":
            try:
                WriteLinkSocial.edit_telegram(new_telegram=link_social.data["telegram"])
                flash("Ссылки на соц сети изменены.")
            except:
                return jsonify({"status": "ok"})
        if link_social.data["instagram"] != "":
            WriteLinkSocial.edit_instagram(new_instagram=link_social.data["instagram"])
            flash("Ссылки на соц сети изменены.")
        if link_social.data["telegram"] == "" and link_social.data["instagram"] == "":
            flash("Поля пустые!")
        return redirect("/admin/")
    return render_template(
        "/admin/main.html",
        images=names_img,
        preview_form=preview_form,
        edit_info_footer=edit_info_footer,
        edit_link_footer=edit_link_footer,
        social=link_social,
        avatar=avatar_title
    )


def admin_price_page():
    # Получаю инфу об услуге. педаю в форму
    link_social = EditLinkSocial()
    condition_form = MyConditionForm()
    condition_form.condition.description = "Я всегда интересуюсь, кто будет присутствовать на съемке, так же могу спросить возраст и имена, чтобы заранее познакомиться со всеми участниками фотосессии."
    za_sutky = MyConditionForm()
    za_sutky.condition.description = "За сутки до начала съемки я напоминаю время и место нашей с вами встречи."
    condition_video = ConditionVideoForm()
    condition_video.text.description = "если вам нужен видеоролик, сообщите мне пожалуйста заранее стоимость видеоролика, продолжительностью до 1 минуты — 2 000₽"
    if request.method == "POST":
        response = request.form.to_dict()
    return render_template("/admin/price.html",
                           social=link_social,
                           condition_form=condition_form,
                           condition_video=condition_video,
                           za_sutky=za_sutky)


def admin_review_page():
    print(__name__)
    return abort(502)


def admin_contacts_page():
    # return render_template(
    #     "contacts.html"
    # )
    print(__name__)
    return abort(502)