import os
import tempfile
import unittest
from pathlib import Path


TEST_DIRECTORY = tempfile.TemporaryDirectory()
os.environ["PET_ADOPTION_DB_PATH"] = str(Path(TEST_DIRECTORY.name) / "test.db")

from init_db import init_db  # noqa: E402
from main import app  # noqa: E402


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config.update(TESTING=True)
        cls.client = app.test_client()

    def test_health_and_seed_data(self):
        self.assertEqual(self.client.get("/").status_code, 200)

        pets = self.client.get("/api/pets").get_json()
        self.assertEqual(len(pets), 24)
        self.assertIn("image", pets[0])

        init_db()
        self.assertEqual(len(self.client.get("/api/pets").get_json()), 24)

    def test_registration_and_login(self):
        response = self.client.post(
            "/api/register",
            json={"name": "test-user", "email": "test@example.com", "password": "secret"},
        )
        self.assertEqual(response.status_code, 201)

        login = self.client.post(
            "/api/login", json={"email": "test@example.com", "password": "secret"}
        )
        self.assertEqual(login.status_code, 200)
        self.assertNotIn("password", login.get_json()["user"])

        invalid = self.client.post(
            "/api/register", json={"name": "missing-password", "email": "bad@example.com"}
        )
        self.assertEqual(invalid.status_code, 400)

    def test_pet_search_and_saved_pet_workflow(self):
        results = self.client.get("/api/pets/search?species=cat").get_json()
        self.assertTrue(results)
        self.assertTrue(all("cat" in pet["species"].lower() for pet in results))

        self.client.delete("/api/pets/1/unsave", json={"user_id": 1})
        first_save = self.client.post("/api/pets/1/save", json={"user_id": 1})
        second_save = self.client.post("/api/pets/1/save", json={"user_id": 1})
        self.assertEqual(first_save.status_code, 200)
        self.assertEqual(second_save.status_code, 200)

        saved = self.client.get("/api/pets/saved/1").get_json()
        self.assertEqual([pet["id"] for pet in saved].count(1), 1)

    def test_questionnaire_and_event_workflows(self):
        questionnaire = self.client.post(
            "/api/questionnaire/submit",
            json={"user_id": 1, "answers": {"0": "30", "1": "active"}},
        )
        self.assertEqual(questionnaire.status_code, 200)

        rsvp = self.client.post("/api/events/1/rsvp", json={"user_id": 1})
        self.assertEqual(rsvp.status_code, 200)
        event_ids = [event["id"] for event in self.client.get("/api/events/rsvped/1").get_json()]
        self.assertIn(1, event_ids)

        removed = self.client.delete("/api/events/1/rsvp", json={"user_id": 1})
        self.assertEqual(removed.status_code, 200)


if __name__ == "__main__":
    unittest.main()
