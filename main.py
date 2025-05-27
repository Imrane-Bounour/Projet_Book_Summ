from book_api import BookAPIClient
from image_display import ImageDisplayer
import requests
from io import BytesIO
from PIL import Image
import os

if __name__ == "__main__":
    client = BookAPIClient()
    livres = client.search_books("Harry Potter")
    print("Livres trouvés :")
    image_paths = []
    for livre in livres:
        titre = livre['volumeInfo'].get('title', 'Titre inconnu')
        print(f"- {titre}")
        image_url = livre['volumeInfo'].get('imageLinks', {}).get('thumbnail')
        if image_url:
            try:
                img_data = requests.get(image_url).content
                img = Image.open(BytesIO(img_data))
                local_path = f"{titre[:20].replace(' ', '_').replace('/', '_')}.jpg"
                img.save(local_path)
                image_paths.append(local_path)
            except Exception as e:
                print(f"Erreur lors du téléchargement de l'image pour {titre}: {e}")
    if image_paths:
        ImageDisplayer.show_images(image_paths)
        # Nettoyage des images téléchargées
        for path in image_paths:
            if os.path.exists(path):
                os.remove(path)