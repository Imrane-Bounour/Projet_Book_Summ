import openai

class LLMClient:
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        openai.api_key = api_key
        self.model = model

    def summarize_text(self, text: str, max_tokens: int = 150) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Tu es un assistant qui résume des textes."},
                {"role": "user", "content": f"Résume ce texte : {text}"}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()

    def ask_question(self, text: str, question: str, max_tokens: int = 100) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Tu es un assistant qui répond à des questions sur un texte."},
                {"role": "user", "content": f"Voici le texte : {text}\nQuestion : {question}"}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()

    def paraphrase_text(self, text: str, max_tokens: int = 150) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Tu es un assistant qui reformule des textes en français."},
                {"role": "user", "content": f"Reformule ce texte : {text}"}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()

    def generate_keywords(self, text: str, max_tokens: int = 60) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Tu es un assistant qui extrait les mots-clés d'un texte en français."},
                {"role": "user", "content": f"Donne les mots-clés de ce texte : {text}"}
            ],
            max_tokens=max_tokens,
            temperature=0.5
        )
        return response.choices[0].message['content'].strip()

    def complete_text(self, prompt: str, max_tokens: int = 100) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Tu es un assistant qui complète des textes en français."},
                {"role": "user", "content": f"Complète ce texte : {prompt}"}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
