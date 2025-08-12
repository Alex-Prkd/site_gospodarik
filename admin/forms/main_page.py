from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired

from admin.forms.BtnFields import ButtonsFields


class PreviewText(FlaskForm):
    text = TextAreaField("Изменить текст", validators=[DataRequired()], description="Инфа из бд")


class EditInfoFooter(ButtonsFields):
    follow_me = TextAreaField("Изменить текст", validators=[DataRequired()], description="Инфа из бд")


class EditLinkFooter(ButtonsFields):
    link = TextAreaField("Изменить ссылку", validators=[DataRequired()], description="Инфа из бд")


class EditLinkSocial(ButtonsFields):
    telegram = StringField(label=f" Изменить ссылку ТГ", description="Инфа из бд")
    instagram = StringField(label=f" Изменить ссылку инстграм", description="Инфа из бд")


