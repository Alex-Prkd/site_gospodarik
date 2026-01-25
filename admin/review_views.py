from flask import jsonify, request

from db.read import ReviewsPage
from db.write import Review


def get_inactive_reviews():
    inactive_reviews = ReviewsPage.get_inactive_reviews()
    inactive_reviews = [review.to_dict() for review in inactive_reviews]
    return jsonify({"inactive_reviews": inactive_reviews}), 200


def accept_inactive_review():
    data = request.get_json()
    Review.accept_inactive_review(data["review_id"])
    return jsonify({"status": True}), 200


def remove_inactive_review():
    data = request.get_json()
    Review.remove_review(data["review_id"])
    return jsonify({"status": True}), 200


def remove_review():
    data = request.get_json()
    Review.remove_review(data["review_id"])
    return jsonify({"status": True}), 200