from PIL import Image
import matplotlib.pyplot as plt

class ImageDisplayer:
    @staticmethod
    def show_image(image_path: str):
        """Affiche une image à partir du chemin donné."""
        img = Image.open(image_path)
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    @staticmethod
    def show_images(image_paths):
        """Affiche plusieurs images à partir d'une liste de chemins."""
        n = len(image_paths)
        fig, axes = plt.subplots(1, n, figsize=(4*n, 4))
        if n == 1:
            axes = [axes]
        for ax, path in zip(axes, image_paths):
            img = Image.open(path)
            ax.imshow(img)
            ax.axis('off')
        plt.show()
