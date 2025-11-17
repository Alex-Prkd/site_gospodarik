import os

from flask import request, jsonify, redirect

from admin.WorkWithImgServices.ConvertSizeIMG import CreateCopySmallSizeIMG
from admin.WorkWithImgServices.RemovePhotoService import RemoveImages
from config import PathImg
from db.write import WriteQuote, WriteInfoFooter, WriteLinkSocial


def add_new_photo():
    data = request.files["file[]"]
    path_big_img, path_middle_img, path_small_size = PathImg.PhotosMainPage()
    data.save(os.path.join(path_big_img, data.filename))
    CreateCopySmallSizeIMG().createMobileIMG(
        name_img=data.filename,
        path_big_img=path_big_img,
        path_middle_img=path_middle_img,
        path_small_img=path_small_size
    )
    return redirect("/admin/")


def remove_photo_view():
    data = request.get_json()
    path_big_img, path_middle_img, path_small_size = PathImg.PhotosMainPage()
    RemoveImages().remove(
        name_img=data["image"],
        path_big_img=path_big_img,
        path_middle_img=path_middle_img,
        path_small_img=path_small_size
    )
    return jsonify({"status": "ok"}), 200



def edit_avatar_photo():
    data = request.files["image"]
    path = PathImg.Link()
    RemoveImages.remove_avatar(path=path)
    data.save(os.path.join(path, data.filename))
    return jsonify({"status": "ok"}), 200


def edit_quote():
    data = request.get_json()
    WriteQuote().edit_quote(new_quote=data["text"])
    return jsonify({"status": "ok"}), 200


def edit_follow_me_text():
    data = request.get_json()
    WriteInfoFooter().edit_info_footer(new_text=data["text"])
    return jsonify({"status": "ok"}), 200


def edit_follow_me_link():
    data = request.get_json()
    WriteInfoFooter().edit_link_footer(link=data["link"])
    return jsonify({"status": "ok"}), 200


def edit_link_telegram():
    data = request.get_json()
    WriteLinkSocial().edit_telegram(new_telegram=data["link_telegram"])
    return jsonify({"status": "ok"}), 200


def edit_link_instagram():
    data = request.get_json()
    WriteLinkSocial().edit_instagram(new_instagram=data["link_instagram"])
    return jsonify({"status": "ok"}), 200

