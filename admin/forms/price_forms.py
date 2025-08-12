from wtforms import StringField, TextAreaField

from admin.forms.BtnFields import ButtonsFields


class MyConditionForm(ButtonsFields):

    condition = TextAreaField("test_area")


class ConditionVideoForm(ButtonsFields):
    text = TextAreaField(description="Инфа из бд")
