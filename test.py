from LLM import LLMClient
import os

# Remplacez par votre clé API OpenAI ou utilisez une variable d'environnement
API_KEY = os.getenv("OPENAI_API_KEY", "votre_cle_api_openai")


def test_summarize_text():
    llm = LLMClient(api_key=API_KEY)
    texte = "Le chat est sur le tapis. Il regarde par la fenêtre et voit un oiseau voler."
    resume = llm.summarize_text(texte)
    print("Résumé :", resume)


def test_ask_question():
    llm = LLMClient(api_key=API_KEY)
    texte = "Le chat est sur le tapis. Il regarde par la fenêtre et voit un oiseau voler."
    question = "Que fait le chat ?"
    reponse = llm.ask_question(texte, question)
    print("Réponse :", reponse)


if __name__ == "__main__":
    test_summarize_text()
    test_ask_question()
