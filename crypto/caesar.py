from helpers import alphabet_position, rotate_character, is_upper_or_lower

def encrypt(text,rot):
    new_text = ''
    for char in range(len(text)):
        new_text = new_text +  rotate_character(text[char],rot)
    return new_text


def main():
    message = input("Enter a message:\n")
    rotation = int(input("Rotate by:\n" ))
    print(encrypt(message,rotation))
if __name__ == "__main__":
    main()