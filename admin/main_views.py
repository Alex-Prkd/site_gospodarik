import os

from flask import request, jsonify, redirect

from admin.ConvertSizeIMG import CreateCopySmallSizeIMG


def add_new_photo():
    response = request.files["file[]"]
    path_photo = os.path.join(os.path.abspath("static/img/photos"))
    response.save(os.path.join(path_photo, response.filename))
    _ = CreateCopySmallSizeIMG(response.filename, path_photo)   # Создаёт копии меньшего размера для телефонов
    return redirect("/admin/")


def remove_photo_view():
    response = request.get_json()
    path = os.path.abspath(f"static/img/photos/{response['image']}")
    path_middle = os.path.abspath(f"static/img/middle_size/{response['image']}")
    path_small = os.path.abspath(f"static/img/small_size/{response['image']}")
    os.remove(os.path.abspath(path))
    os.remove(os.path.abspath(path_middle))
    os.remove(os.path.abspath(path_small))
    return jsonify({"status": "ok"}), 200



def edit_avatar_photo():
    # Удаляем старую аватарку и сохраняем новую
    response = request.files["image"]
    path_avatar = os.path.abspath("static\img\link")
    old_avatar = os.listdir(path_avatar)[0]
    os.remove(os.path.join(path_avatar, old_avatar))
    response.save(os.path.join(path_avatar, response.filename))
    return jsonify({"status": "ok"}), 200