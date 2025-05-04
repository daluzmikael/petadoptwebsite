@extra_api.route('/questionnaire/submit', methods=['POST'])
def submit_questionnaire():
    data = request.get_json()
    user_id = data.get("user_id")
    responses = data.get("responses")  # should be a list of {"question": q, "answer": a}

    if not user_id or not isinstance(responses, list):
        return jsonify({"error": "Invalid request"}), 400

    conn = get_connection()
    c = conn.cursor()
    c.executemany(
        "INSERT INTO questionnaire_responses (user_id, question, answer) VALUES (?, ?, ?)",
        [(user_id, r["question"], r["answer"]) for r in responses]
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Questionnaire submitted"})
