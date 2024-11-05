from flask import Blueprint, request, jsonify, current_app
from ultralytics import YOLO

classifier_service = Blueprint("classifier", __name__)

model = YOLO("yolo11n-cls.pt")

@classifier_service.route("/classify", methods=["POST"])
def classify():
    data = request.files["image"]
    results = model(data)
    return jsonify(results)