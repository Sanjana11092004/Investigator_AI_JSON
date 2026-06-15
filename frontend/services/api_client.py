import requests


class APIClient:

    def __init__(self):
        self.base_url = "http://localhost:8000"

    def get_backend_status(self):
        try:
            response = requests.get(
                f"{self.base_url}/health",
                timeout=5
            )

            return response.status_code == 200

        except Exception:
            return False

    def send_message(self, question, session_id):

        payload = {
            "question": question,
            "session_id": session_id
        }

        response = requests.post(
            f"{self.base_url}/investigator/chat",
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        return response.json()

    def get_dashboard_stats(self):

        response = requests.get(
            f"{self.base_url}/dashboard/stats"
        )

        response.raise_for_status()

        return response.json()

    def get_documents(self):

        response = requests.get(
            f"{self.base_url}/dashboard/documents"
        )

        response.raise_for_status()

        return response.json()

    def upload_file(self, file):

        files = {
            "file": (
                file.name,
                file,
                file.type
            )
        }

        response = requests.post(
            f"{self.base_url}/upload/upload",
            files=files,
            timeout=300
        )

        response.raise_for_status()

        return response.json()