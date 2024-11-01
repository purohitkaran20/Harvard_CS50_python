import os
import sys
from PIL import Image, ImageOps

def validate_arguments(arguments, files):
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 3:
        sys.exit("Too many command-line arguments")
    before = arguments[1]
    after = arguments[2]

    # Check if both input and output files have valid image extensions
    if not before.endswith((".jpg", ".jpeg", ".png")) or not after.endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

    # Use splitext to get the extensions and compare them
    before_ext = os.path.splitext(before)[1].lower()
    after_ext = os.path.splitext(after)[1].lower()

    if before_ext != after_ext:
        sys.exit("Input and output have different extensions")

    if before not in files:
        sys.exit(f"Input does not exist")


def wear_tshirt(before, after):
        # Open the shirt image and the user-provided image
        shirt = Image.open("shirt.png")
        user_image = Image.open(before)

        # Get the size of the shirt image
        size = shirt.size

        # Resize/crop the user image to match the shirt size
        user_image = ImageOps.fit(user_image, size)

        # Overlay the user image on top of the shirt image
        user_image.paste(shirt, (0, 0), shirt)

        # Save the final composite image
        user_image.save(after)



def main():
    files = os.listdir(".")
    validate_arguments(sys.argv, files)
    before = sys.argv[1]
    after = sys.argv[2]
    wear_tshirt(before, after)

if __name__ == "__main__":
    main()
