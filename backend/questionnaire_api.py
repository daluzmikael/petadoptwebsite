from flask import Blueprint, jsonify, request
from db import get_questionnaire_responses, save_questionnaire_responses
questionnaire_api = Blueprint('questionnaire_api', __name__)

@questionnaire_api.route('/questionnaire/submit', methods=['POST'])
def submit_questionnaire():
    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id")
    responses = data.get("responses") or data.get("answers")

    if not user_id or not isinstance(responses, (dict, list)):
        return jsonify({"error": "Invalid request"}), 400

    if isinstance(responses, dict):
        formatted = [(f"Q{idx}", str(answer)) for idx, answer in responses.items()]
    else:
        try:
            formatted = [(str(item["question"]), str(item["answer"])) for item in responses]
        except (KeyError, TypeError):
            return jsonify({"error": "Invalid responses"}), 400

    save_questionnaire_responses(user_id, formatted)

    return jsonify({"message": "Questionnaire submitted"})

@questionnaire_api.route('/questionnaire/all', methods=['GET'])
def get_all_responses():
    try:
        responses = get_questionnaire_responses()
        return jsonify(responses)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
