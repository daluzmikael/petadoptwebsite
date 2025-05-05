from flask import Blueprint, jsonify, request
from db import save_rsvp_for_user, get_rsvped_events_for_user, get_connection
import json

extra_api = Blueprint('extra_api', __name__)

# Application Status & Notifications 
@extra_api.route('/application/status', methods=['GET'])
def get_application_status():
    return jsonify({"status": "In Review", "last_updated": "2025-04-09"})

@extra_api.route('/notifications', methods=['GET'])
def get_notifications():
    return jsonify([
        {"message": "Application received", "date": "2025-04-08"},
        {"message": "Profile updated", "date": "2025-04-07"}
    ])

# Digital Paperwork 
@extra_api.route('/documents', methods=['GET'])
def get_documents():
    return jsonify([
        {"id": 1, "title": "Adoption Agreement", "status": "Incomplete"},
        {"id": 2, "title": "Home Visit Form", "status": "Submitted"}
    ])

@extra_api.route('/documents', methods=['POST'])
def upload_document():
    return jsonify({"message": "Document uploaded successfully"})

# Adoption Process Tracker 
@extra_api.route('/adoption/status', methods=['GET'])
def get_adoption_status():
    return jsonify({
        "steps": [
            {"name": "Application Submitted", "complete": True},
            {"name": "Home Visit Scheduled", "complete": False},
            {"name": "Final Approval", "complete": False}
        ]
    })

# Events API
@extra_api.route('/events', methods=['GET'])
def get_events():
    return jsonify([
        {"id": 1, "name": "Spring Pet Fair", "date": "2025-05-01"},
        {"id": 2, "name": "Adoption Meet & Greet", "date": "2025-05-15"},
        {"id": 3, "name": "Puppy Yoga", "date": "2025-05-10"}
    ])

@extra_api.route('/events/<int:event_id>/rsvp', methods=['POST'])
def rsvp_event(event_id):
    data = request.get_json()
    user_id = data.get("user_id")
    if not user_id:
        return jsonify({"error": "User ID required"}), 400
    save_rsvp_for_user(user_id, event_id)
    return jsonify({"message": f"RSVP saved for event {event_id}"}), 200

@extra_api.route('/events/rsvped/<int:user_id>', methods=['GET'])
def get_user_rsvped_events(user_id):
    events = get_rsvped_events_for_user(user_id)
    return jsonify(events)

@extra_api.route('/events/<int:event_id>/rsvp', methods=['DELETE'])
def un_rsvp_event(event_id):
    data = request.get_json()
    user_id = data.get("user_id")
    if not user_id:
        return jsonify({"error": "User ID required"}), 400

    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM rsvped_events WHERE user_id = ? AND event_id = ?", (user_id, event_id))
    conn.commit()
    conn.close()

    return jsonify({"message": f"RSVP removed for event {event_id}"}), 200

