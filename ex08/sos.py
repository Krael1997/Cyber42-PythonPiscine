import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ' ':'/', 
                  } 

def morse_encode(message):
    encoded_message = []
    for char in message:
        encoded_char = MORSE_CODE_DICT.get(char.upper())
        if encoded_char:
            encoded_message.append(encoded_char)
        else:
            return None
    return ' '.join(encoded_message)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: python3 sos.py message")
    else:
        encoded_message = []
        for message in sys.argv[1:]:
            encoded = morse_encode(message)
            if encoded:
                encoded_message.append(encoded)
            else:
                print("ERROR")
                sys.exit(1)
        print(' '.join(encoded_message))
