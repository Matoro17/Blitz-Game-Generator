import svgwrite
import os
import io
import cairosvg
from PIL import Image
from xml.dom import minidom

# Function to create SVG images based on input parameters
def create_svg(path1, color1, path2, color2, idx):
    # Create SVG drawing
    svg_document = svgwrite.Drawing(size=("56mm", "87mm"))

    # Create rectangles to serve as card background
    background_rect = svgwrite.shapes.Rect(insert=(0, 0), size=("100%", "100%"), fill="white")
    svg_document.add(background_rect)

    # Define object positions
    object1_x, object1_y = 5, 5  # Adjust as needed
    object2_x, object2_y = 31, 5  # Adjust as needed

    # Add object 1
    object1_path = svgwrite.path.Path(d=path1, fill=color1)
    object1_path.translate(object1_x, object1_y)
    svg_document.add(object1_path)

    # Add object 2
    object2_path = svgwrite.path.Path(d=path2, fill=color2)
    object2_path.translate(object2_x, object2_y)
    svg_document.add(object2_path)

    # Add labels for objects
    label_font_size = "8pt"
    object1_label = svgwrite.text.Text(os.path.basename(path1), insert=(object1_x, 30), font_size=label_font_size)
    object2_label = svgwrite.text.Text(os.path.basename(path2), insert=(object2_x, 30), font_size=label_font_size)
    svg_document.add(object1_label)
    svg_document.add(object2_label)

    # Save SVG to PNG
    svg_path = f"card_{idx}.svg"
    svg_document.saveas(svg_path)

    # Convert SVG to PNG
    png_bytes = cairosvg.svg2png(url=svg_path)

    # Open PNG image from bytes
    img = Image.open(io.BytesIO(png_bytes))

    # Save PNG
    img.save(f"export/card_{idx}.png", "PNG")

    # Remove temporary SVG file
    os.remove(svg_path)

# Function to read combinations from a text file and generate images
def generate_images(text_file):
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

            # Extract path data from SVG files
            path1 = extract_svg_path(f'svgs/{object1}.svg')
            path2 = extract_svg_path(f'svgs/{object2}.svg')

            if path1 is None or path2 is None:
                print(f"Failed to extract path data for line {idx}: {line}. Skipping...")
                continue

            create_svg(path1, color1, path2, color2, idx)

# Function to extract SVG path data from an SVG file
def extract_svg_path(svg_file):
    try:
        doc = minidom.parse(svg_file)
        path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
        if len(path_strings) > 0:
            return path_strings[0]
        else:
            return None
    except Exception as e:
        print(f"Failed to extract path data from SVG file {svg_file}: {e}")
        return None

# Path to the text file containing combinations
text_file = "complete_deck.txt"
# Call the function to generate images
generate_images(text_file)