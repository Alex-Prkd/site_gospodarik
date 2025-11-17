import os.path

import requests
from flask import jsonify, request, json, abort

from admin.WorkWithImgServices.ConvertSizeIMG import CreateCopySmallSizeIMG
from admin.WorkWithImgServices.RemovePhotoService import RemoveImages
from config import PathImg
from db.write import WriteNewService, EditService, RemoveServiceDB, EditStageWorkDB, MyConditionDB, ConditionVideoDB, \
    AdditionalInfoDB, DiscountDB, OrderPhotoShootDB


def add_service():
    title = request.form.get("title")
    price = request.form.get("price")
    descriptions = json.loads(request.form.get("descriptions", "[]"))
    image = request.files.get("image")
    transaction = WriteNewService().add_service(
        title=title,
        descriptions=descriptions,
        img_title=image.filename,
        price=int(price)
    )
    if transaction:
        path_big_img, path_middle_img, path_small_img = PathImg.Services()
        image.save(os.path.join(path_big_img, image.filename))
        CreateCopySmallSizeIMG().createMobileIMG(
            name_img=image.filename,
            path_big_img=path_big_img,
            path_middle_img=path_middle_img,
            path_small_img=path_small_img
        )
    return jsonify({"status": True}), 200


def edit_title_service():
    data = request.get_json()
    EditService.edit_title(data["id"], data["title"])
    return jsonify({"status": True}), 200


def edit_img_service():
    old_img = request.form.get("old_img")
    new_img = request.files.get("new_photo")
    path_big_img, path_middle_img, path_small_img = PathImg.Services()
    transaction = EditService.edit_img_service(old_img, new_img.filename)
    if transaction:
        new_img.save(os.path.join(path_big_img, new_img.filename))
        RemoveImages().remove(
            name_img=old_img,
            path_big_img=path_big_img,
            path_middle_img=path_middle_img,
            path_small_img=path_small_img
        )
        CreateCopySmallSizeIMG().createMobileIMG(
            name_img=new_img.filename,
            path_big_img=path_big_img,
            path_middle_img=path_middle_img,
            path_small_img=path_small_img
        )
    return jsonify({"status": True}), 200


def edit_description_service():
    data = request.get_json()
    EditService.edit_description(data["info_id"], data["new_description"])
    return jsonify({"status": True}), 200


def edit_price_service():
    data = request.get_json()
    EditService.edit_price(data["service_id"], data["new_price"])
    return jsonify({"status": True}), 200


def add_new_description_service():
    data = request.get_json()
    info_id: int = EditService.add_description(data["service_id"], text=data["description"])
    return jsonify({"status": True, "info_id": info_id}), 200


def remove_descriptions_service():
    data = request.get_json()
    EditService.remove_descriptions(data["descriptions_id"])
    return jsonify({"status": True}), 200


def remove_service():
    data = request.get_json()
    path_big_img, path_middle_img, path_small_img = PathImg.Services()
    title_img = RemoveServiceDB.remove(data["service_id"])
    RemoveImages().remove(
        name_img=title_img,
        path_big_img=path_big_img,
        path_middle_img=path_middle_img,
        path_small_img=path_small_img
    )
    return jsonify({"status": True}), 200


def remove_condition():
    data = request.get_json()
    EditStageWorkDB.remove_condition(data["condition_id"])
    return jsonify({"status": True}), 200


def create_new_stage_work():
    data = request.get_json()
    EditStageWorkDB.new_stage_work(data["stage_title"], data["conditions"])
    return jsonify({"status": True}), 200


def edit_stage():
    data = request.get_json()
    start_change = EditStageWorkDB()
    for method_name, values in data["data_for_editing"].items():
        method = getattr(start_change, method_name)
        method(values)
    return jsonify({"status": True}), 200


def new_condition_stage():
    data = request.get_json()
    EditStageWorkDB.new_condition(**data)
    return jsonify({"status": True}), 200


def remove_stage():
    data = request.get_json()
    EditStageWorkDB.remove_stage(data["stage_id"])
    return jsonify({"status": True}), 200


def add_new_my_condition():
    data = request.get_json()
    MyConditionDB.create(data["new_condition"])
    return jsonify({"status": True}), 200


def change_my_condition():
    data = request.get_json()
    MyConditionDB.edit(data["condition_id"], data["text"])
    return jsonify({"status": True}), 200


def remove_my_condition():
    data = request.get_json()
    MyConditionDB.remove(data["condition_id"])
    return jsonify({"status": True}), 200


def change_condition_video():
    data = request.get_json()
    ConditionVideoDB.edit(data["id"], data["text"])
    return jsonify({"status": True}), 200


def edit_background_photo_price_page():
    data = request.files
    path_bg_image = PathImg.BackgroundPricePage()
    bg_image = os.listdir(path_bg_image)[0]     # Проверить на искл., если папка пуста
    if os.path.exists(os.path.join(path_bg_image, bg_image)):
        os.remove(os.path.join(path_bg_image, bg_image))
    image = data.get("photo_bg")
    image.save(os.path.join(path_bg_image, image.filename))
    return jsonify({"status": True}), 200


def edit_info_footer():
    data = request.get_json()
    AdditionalInfoDB.edit(data["id"], data["text"])
    return jsonify({"status": True}), 200


def remove_info_footer():
    data = request.get_json()
    AdditionalInfoDB.remove(data["id"])
    return jsonify({"status": True}), 200


def add_new_info_footer():
    data = request.get_json()
    AdditionalInfoDB.create(data["text"])
    return jsonify({"status": True}), 200


def edit_discount():
    data = request.get_json()
    DiscountDB.edit(data["id"], data["text"])
    return jsonify({"status": True}), 200


def remove_discount():
    data = request.get_json()
    DiscountDB.remove(data["id"])
    return jsonify({"status": True}), 200


def add_new_discount():
    data = request.get_json()
    DiscountDB.create(data["text"])
    return jsonify({"status": True}), 200


def edit_order_text():
    data = request.get_json()
    OrderPhotoShootDB.edit(data["text"])
    return jsonify({"status": True}), 200