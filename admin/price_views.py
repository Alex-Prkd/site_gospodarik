from flask import render_template, flash, abort, jsonify

from admin.forms.main_page import EditLinkSocial
from admin.forms.price_forms import MyConditionForm, ConditionVideoForm


def remove_service():
    print(remove_service.__name__)
    return jsonify({"status": True, "msg": "Услуга удалена."}), 200


def edit_before_work():
    pass