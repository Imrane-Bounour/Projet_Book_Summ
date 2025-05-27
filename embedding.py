import openai
from typing import List

class EmbeddingClient:
    def __init__(self, api_key: str, model: str = "text-embedding-ada-002"):
        openai.api_key = api_key
        self.model = model

    def get_embedding(self, text: str) -> List[float]:
        response = openai.Embedding.create(
            input=text,
            model=self.model
        )
        return response['data'][0]['embedding']

    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        response = openai.Embedding.create(
            input=texts,
            model=self.model
        )
        return [item['embedding'] for item in response['data']]
