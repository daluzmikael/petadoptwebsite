from flask import Blueprint, jsonify, request

extra_api = Blueprint('extra_api', __name__)

# Application Status & Notifications 

@extra_api.route('/api/application/status', methods=['GET'])
def get_application_status():
    return jsonify({"status": "In Review", "last_updated": "2025-04-09"})

@extra_api.route('/api/notifications', methods=['GET'])
def get_notifications():
    return jsonify([
        {"message": "Application received", "date": "2025-04-08"},
        {"message": "Profile updated", "date": "2025-04-07"}
    ])


# Digital Paperwork 

@extra_api.route('/api/documents', methods=['GET'])
def get_documents():
    return jsonify([
        {"id": 1, "title": "Adoption Agreement", "status": "Incomplete"},
        {"id": 2, "title": "Home Visit Form", "status": "Submitted"}
    ])

@extra_api.route('/api/documents', methods=['POST'])
def upload_document():
    return jsonify({"message": "Document uploaded successfully"})


# Adoption Process Tracker 

@extra_api.route('/api/adoption/status', methods=['GET'])
def get_adoption_status():
    return jsonify({
        "steps": [
            {"name": "Application Submitted", "complete": True},
            {"name": "Home Visit Scheduled", "complete": False},
            {"name": "Final Approval", "complete": False}
        ]
    })


# Events: RSVP and Check-In 

@extra_api.route('/api/events', methods=['GET'])
def get_events():
    return jsonify([
        {"id": 1, "name": "Spring Pet Fair", "date": "2025-05-01"},
        {"id": 2, "name": "Adoption Meet & Greet", "date": "2025-05-15"}
    ])

@extra_api.route('/api/events/<int:event_id>/rsvp', methods=['POST'])
def rsvp_event(event_id):
    return jsonify({"message": f"RSVP received for event {event_id}"})

@extra_api.route('/api/events/<int:event_id>/checkin', methods=['POST'])
def checkin_event(event_id):
    return jsonify({"message": f"Checked in for event {event_id}"})

