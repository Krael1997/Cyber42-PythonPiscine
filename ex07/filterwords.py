import sys
import string

if len(sys.argv) != 3:
    print("ERROR")
else:
    try:
        s = sys.argv[1]
        n = int(sys.argv[2])
        exclude = string.punctuation
        words = [w.strip(exclude) for w in s.split() if len(w.strip(exclude)) > n]
        print(words)
    except:
        print("ERROR")
