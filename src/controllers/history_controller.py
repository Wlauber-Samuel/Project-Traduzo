from flask import Blueprint, jsonify
from src.models.history_model import HistoryModel


history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def index():
    get_history = HistoryModel.list_as_json()
    return jsonify(get_history), 200
