from PIL import Image
import numpy as np

class TraitementImage:
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image = Image.open(image_path)

    def to_grayscale(self):
        """Convertit l'image en niveaux de gris."""
        return self.image.convert('L')

    def resize(self, size):
        """Redimensionne l'image à la taille donnée (largeur, hauteur)."""
        return self.image.resize(size)

    def get_array(self):
        """Retourne l'image sous forme de tableau numpy."""
        return np.array(self.image)

    def save(self, output_path):
        """Sauvegarde l'image actuelle à l'emplacement spécifié."""
        self.image.save(output_path)
