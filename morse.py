morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Reverse Morse code dictionary
reverse_morse_code_dict = {value: key for key, value in morse_code_dict.items()}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += ' '
    return morse_code.strip()

def morse_to_text(morse_code):
    text = ''
    morse_words = morse_code.split(' / ')
    for word in morse_words:
        morse_chars = word.split()
        for char in morse_chars:
            if char in reverse_morse_code_dict:
                text += reverse_morse_code_dict[char]
            else:
                text += ' '
        text += ' '
    return text.strip()

def morse():
    while True:
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter the text to convert to Morse code: ")
            morse_code = text_to_morse(text)
            print(text, "In Morse Code:", morse_code)
        elif choice == '2':
            morse_code = input("Enter the Morse code to convert to text: ")
            text = morse_to_text(morse_code)
            print("Text:", text)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

morse()         