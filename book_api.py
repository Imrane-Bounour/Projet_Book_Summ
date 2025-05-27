import requests

class BookAPIClient:
    def __init__(self, base_url="https://www.googleapis.com/books/v1/volumes"):
        self.base_url = base_url

    def search_books(self, query, max_results=5):
        params = {
            'q': query,
            'maxResults': max_results
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json().get('items', [])
        else:
            print(f"Erreur lors de la récupération des livres: {response.status_code}")
            return []

    def get_book_info(self, book_id):
        url = f"{self.base_url}/{book_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erreur lors de la récupération du livre: {response.status_code}")
            return None
