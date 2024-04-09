import os
import io
from PIL import Image, ImageDraw

# Function to create PNG images based on input parameters
def create_card(object1_path, color1, object2_path, color2, idx):
    # Load PNG images
    object1_img = Image.open(object1_path)
    object2_img = Image.open(object2_path)

    card_width, card_height = 560, 870

    # Resize images
    resized_width = card_width
    resized_height = card_height/2  
    object1_img_resized = object1_img.resize((resized_width, resized_height))
    object2_img_resized = object2_img.resize((resized_width, resized_height))

    # Create a new blank image for the card with a white background
    card = Image.new('RGB', (card_width, card_height), color='white')

    # Paste object1 onto the card and colorize it
    object1_colored = colorize_image(object1_img_resized, color1)
    card.paste(object1_colored, (0, 0))

    # Paste object2 onto the card and colorize it
    object2_colored = colorize_image(object2_img_resized, color2)
    card.paste(object2_colored, (0, card_height // 2))

    # Save the card as a PNG file
    card_path = f"export/card_{idx}.png"
    card.save(card_path)

def colorize_image(image, color):
    # Create a solid color image the same size as the original image
    color_image = Image.new('RGBA', image.size, color)
    
    # Composite the original image with the solid color using alpha blending
    return Image.alpha_composite(color_image, image.convert('RGBA'))

def generate_cards(text_file):
    with open(text_file, 'r') as f:
        lines = f.readlines()[1:]  # Skip the first line
        for idx, line in enumerate(lines, start=1):  # Start counting from line 1
            line = line.strip().split(' - ')
            if len(line) != 2:
                print(f"Illegal line format in line {idx}: {line}. Skipping...")
                continue
            objects = line[0].split(' (')
            if len(objects) != 2:
                print(f"Illegal line format in line {idx}: {line}. Skipping...")
                continue
            object1 = objects[0]
            color1 = objects[1][:-1].lower()
            objects = line[1].split(' (')
            if len(objects) != 2:
                print(f"Illegal line format in line {idx}: {line}. Skipping...")
                continue
            object2 = objects[0]
            color2 = objects[1][:-1].lower()
            create_card(f"pngs2/{object1.lower()}.png", color1, f"pngs2/{object2.lower()}.png", color2, idx)

# Path to the text file containing combinations
text_file = "complete_deck.txt"
# Call the function to generate cards
generate_cards(text_file)
