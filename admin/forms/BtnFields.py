from flask_wtf import FlaskForm
from wtforms import SubmitField


class ButtonsFields(FlaskForm):
    remove_btn = SubmitField("Удалить")
    save_btn = SubmitField("Сохранить")
    edit_btn = SubmitField("Изменить")