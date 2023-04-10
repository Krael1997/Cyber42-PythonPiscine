import sys

def text_analyzer(text=None):
    """
    Esta funcion cuenta el numero de caracteres mayus, de caracteres minus, puntos y espacios es un texto.
    """
    if text is None:
        text = input("What is the text to analyze?\n")

    if not isinstance(text, str):
        raise Assertionerror("argument is not a string")

    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in '.,:;!?')
    spaces = sum(1 for c in text if c.isspace())

    print(f"The text contains {len(text)} character(s):\n"
            f"- {upper} upper letter(s)\n"
            f"- {lower} lower letter(s)\n"
            f"- {punct} punctuation mark(s)\n"
            f"- {spaces} space(s)")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Error: too many arguments")
    elif len(sys.argv) == 2:
        try:
            text_analyzer(sys.argv[1])
        except Assertionerror as e:
            print(e)
    else:
            text_analyzer()
