import pyfiglet
import termcolor

def display_logo():
    logo_text = "ASCII ART"
    ascii_logo = pyfiglet.figlet_format(logo_text, font="slant")
    colored_logo = termcolor.colored(ascii_logo, "cyan")
    print(colored_logo)

if __name__ == "__main__":
    display_logo()
