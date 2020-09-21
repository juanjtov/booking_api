import json

from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.db import get_reviews_by_hotel, get_reviews_by_user, set_review, update_review, delete_review
from app.booking.models import Review


class ReviewsResource(Resource):
    """
    """
    @jwt_required
    def get(self):
        body = request.get_json()
        get_by = str(body.get('get_by'))

        if get_by == 'hotel':
            hotel_id = int(body.get('hotel_id'))
            reviews_fetched, e = get_reviews_by_hotel(hotel_id)

            print('reviews: ', reviews_fetched)

            reviews = []
            for review in reviews_fetched:
                reviews.append(Review(**review))

            return jsonify(reviews=[review.serialize() for review in reviews])
        elif get_by == 'user':
            user_id = int(body.get('user_id'))
            reviews_fetched, e = get_reviews_by_user(user_id)

            print('reviews: ', reviews_fetched)

            reviews = []
            for review in reviews_fetched:
                reviews.append(Review(**review))

            return jsonify(reviews=[review.serialize() for review in reviews])

    @jwt_required
    def post(self):
        body = request.get_json()
        review = Review(**body)

        process_msg, e = set_review(review)
        if e != 1062:
            return process_msg
        else:
            return {'error': f'Review {review.review_id} already exists'}       


    @jwt_required
    def put(self):
        body = request.get_json()
        review = Review(**body)

        process_msg, e = update_review(review)
        return process_msg
       
    @jwt_required
    def delete(self):
        body = request.get_json()
        review_id = int(body.get('review_id'))
        process_msg = delete_review(review_id)
        return process_msg
        