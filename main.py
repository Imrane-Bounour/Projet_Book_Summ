from book_api import BookAPIClient

if __name__ == "__main__":
    client = BookAPIClient()
    livres = client.search_books("Harry Potter")
    print("Livres trouvés :")
    for livre in livres:
        titre = livre['volumeInfo'].get('title', 'Titre inconnu')
        print(f"- {titre}")