from flask import request, jsonify

from db.write import PreviewTextContactPageDB


def save_preview_text():
    data = request.get_json()
    PreviewTextContactPageDB.edit_text(new_text=data["new_preview"])
    return jsonify({"status": True}), 200