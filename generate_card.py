import svgwrite
import cairosvg
from io import BytesIO
from io import StringIO


def colorize_svg(svg_content, color='#FF0000'):

    with open(svg_content, 'r') as svg_file2:
        svg_content2 = svg_file2.read()
    # Create an in-memory SVG file
    svg_file = StringIO(svg_content2)

    # Read the SVG content
    with svg_file as f:
        content = f.read()

    # Modify SVG content to apply color
    print(content)
    colored_svg_content = content.replace('<svg', f'<svg fill="{color}"')

    return colored_svg_content

def combine_images(input_svg1, input_svg2, output_svg):
    color1 = '#00FF00'  # Color for the first SVG, change as needed
    color2 = '#0000FF'  # Color for the second SVG, change as needed

    # Colorize each SVG
    svg_content1 = colorize_svg(input_svg1, color=color1)
    svg_content2 = colorize_svg(input_svg2, color=color2)

    # Combine the SVG content into a single SVG
    combined_svg_content = f"<svg>{svg_content1}{svg_content2}</svg>"


    with open(output_svg, 'w') as output_file:
        output_file.write(combined_svg_content)


if __name__ == "__main__":
    svg_file1 = 'svgs/bottle.svg'  # Replace with the path to your first SVG file
    svg_file2 = 'svgs/flower.svg'  # Replace with the path to your second SVG file
    output_png_file = 'combined_output.svg'

    combine_images(svg_file1, svg_file2, output_png_file)

    print(f"SVG files '{svg_file1}' and '{svg_file2}' combined and saved to PNG: '{output_png_file}'.")
