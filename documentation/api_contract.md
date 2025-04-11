
API Contract — Milestone 5
===========================

Team 16 Spring 2025  
API Contract  
Date: April 10, 2025

Pet Endpoints
----------------

GET /api/pets  
Input: None  
Output: JSON list of pet objects  
Example:
[
  {"id": 1, "name": "Buddy", "species": "Dog", "breed": "Labrador"},
  {"id": 2, "name": "Whiskers", "species": "Cat", "breed": "Siamese"}
]

GET /api/pets/<int:pet_id>  
Input: Path variable pet_id (Integer)  
Output: JSON pet object or error  
Example:
{"id": 1, "name": "Buddy", "species": "Dog", "breed": "Labrador"}

POST /api/pets/<int:pet_id>/save  
Input: Path variable pet_id  
Output:
{"message": "Pet <pet_id> saved."}

GET /api/pets/saved  
Input: None  
Output: List of saved pets  
Example:
[]

GET /api/pets/search?species=dog  
Input: Query parameter species (String)  
Output: Filtered list of pet objects

User Endpoints
------------------

POST /api/register  
Input:
{
  "name": "string",
  "email": "string",
  "password": "string"
}
Output: Echo of input JSON

POST /api/login  
Input:
{
  "email": "string",
  "password": "string"
}
Output:
{"message": "Logged in"}

GET /api/profile  
Input: None  
Output:
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}

PUT /api/profile  
Input:
{
  "name": "New Name",
  "email": "new@example.com"
}
Output: Echo of updated user object

Application & Event Endpoints (Mocked)
-----------------------------------------

GET /api/application/status  
Output:
{
  "status": "In Review",
  "last_updated": "2025-04-09"
}

GET /api/notifications  
Output:
[
  {"message": "Application received", "date": "2025-04-08"},
  {"message": "Profile updated", "date": "2025-04-07"}
]

GET /api/documents  
Output:
[
  {"id": 1, "title": "Adoption Agreement", "status": "Incomplete"},
  {"id": 2, "title": "Home Visit Form", "status": "Submitted"}
]

POST /api/documents  
Input: File/document metadata (mocked only)  
Output:
{"message": "Document uploaded successfully"}

GET /api/adoption/status  
Output:
{
  "steps": [
    {"name": "Application Submitted", "complete": true},
    {"name": "Home Visit Scheduled", "complete": false},
    {"name": "Final Approval", "complete": false}
  ]
}

GET /api/events  
Output:
[
  {"id": 1, "name": "Spring Pet Fair", "date": "2025-05-01"}
]

POST /api/events/<int:event_id>/rsvp  
Output:
{"message": "RSVP received for event <event_id>"}

POST /api/events/<int:event_id>/checkin  
Output:
{"message": "Checked in for event <event_id>"}

Notes
-----
- All endpoints currently return mocked/stubbed data.
- Input validation, authentication, and real persistence will be implemented in later milestones.

