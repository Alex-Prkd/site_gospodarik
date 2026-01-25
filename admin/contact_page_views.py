import functools
import os

from flask import request, jsonify

from admin.WorkWithImgServices.RemovePhotoService import RemoveImages
from config import PathImg
from db.write import PreviewTextContactPageDB, TextContactMeContactPageDB


def save_preview_text():
    data = request.get_json()
    PreviewTextContactPageDB.edit_text(new_text=data["new_preview"])
    return jsonify({"status": True}), 200


def save_preview_avatar():
    data = request.files["image"]
    path_photo = PathImg.ContactPageAvatar()
    contact_avatar = os.listdir(path_photo)
    RemoveImages.remove_contact_page_preview(path_photo, contact_avatar)
    data.save(os.path.join(path_photo, "avatar.jpg"))
    return jsonify({"status": True}), 200


def save_background():
    data = request.files["background"]
    path_background = PathImg.ContactPageBackground()
    background = os.listdir(path_background)
    RemoveImages.remove_contact_page_background(path_background, background)
    data.save(os.path.join(path_background, "background.jpg"))
    return jsonify({"status": True}), 200


def save_title_contact_me():
    data = request.get_json()
    TextContactMeContactPageDB.edit_title_text(new_title=data["text"])
    return jsonify({"status": True}), 200


def save_text_contact_me():
    data = request.get_json()
    TextContactMeContactPageDB.edit_info(new_text=data["text"])
    return jsonify({"status": True}), 200


def save_number_contact_me():
    data = request.get_json()
    TextContactMeContactPageDB.edit_number(new_number=data["number"])
    return jsonify({"status": True}), 200


