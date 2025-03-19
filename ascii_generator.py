import pyfiglet
import termcolor
import requests
from PIL import Image
import io
import numpy as np

def text_to_ascii(text, font="slant", color="white"):
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        colored_art = termcolor.colored(ascii_art, color)
        return colored_art
    except Exception as e:
        return f"Error: {e}"

def image_to_ascii(url, width=100):
    try:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        image = image.convert("L")  # Convert to grayscale
        aspect_ratio = image.height / image.width
        new_height = int(width * aspect_ratio)
        image = image.resize((width, new_height))
        
        chars = np.array(list(" .:-=+*#%@"))
        pixels = np.array(image)
        ascii_image = "\n".join("".join(chars[pixel // 25] for pixel in row) for row in pixels)
        return ascii_image
    except Exception as e:
        return f"Error: {e}"

def main():
    print("ASCII Art Generator")
    print("1. Convert Text to ASCII")
    print("2. Convert Image URL to ASCII")
    choice = input("Choose an option (1/2): ")
    
    if choice == "1":
        text = input("Enter text: ")
        font = input("Enter font (default: slant): ") or "slant"
        color = input("Enter color (default: white): ") or "white"
        print(text_to_ascii(text, font, color))
    
    elif choice == "2":
        url = input("Enter image URL: ")
        print(image_to_ascii(url))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
