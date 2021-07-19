import zipfile

class BruteForce:
    def __init__(self, zip_file, wordlist):
        self.zip_file = zip_file
        self.wordlist = wordlist

    def zip_brute(self):
        zip_file = zipfile.ZipFile(self.zip_file)
        n_words = len(list(open(self.wordlist, "rb")))
        print("Loading Wordlist")
        print(f"\n{n_words} Passwords Have Been Loaded")

        with open(self.wordlist, "rb") as wordlist:
            for index, word in enumerate(wordlist):
                try:
                    print(index+1, "Trying Password ", str(word.decode()))
                    zip_file.extractall(pwd=word.strip())
                    print("\nPassword found ----> ", word.decode())
                    break
                except KeyboardInterrupt:
                    print("\nKeyboardInterrupt")
                except Exception as e:
                    continue
