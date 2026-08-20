from PIL import Image
from pathlib import Path

# Mapp med bilder
input_folder = Path("images")

# Max storlek
MAX_SIZE = (500, 500)

for file in input_folder.iterdir():

    if file.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp"]:
        continue

    with Image.open(file) as img:

        img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)

        img.save(file, optimize=True)

        print(f"{file.name} -> {img.width}x{img.height}")

print("Klart!")