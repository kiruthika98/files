def vowelz(a):
        vowels = ["a", "e", "i", "o", "u"]
        vowel = False
        for vowell in vowels:
                if vowell in a:
                        vowel = True
        print vowel
vowelz(raw_input("Enter a word:"))
