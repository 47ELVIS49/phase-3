class CLI:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Add a new word")
            print("2. Look up a word")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_word()
            elif choice == '2':
                self.lookup_word()
            elif choice == '3':
                print("\nExiting the program. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")

    def add_word(self):
        print("\nADD WORD TO DICTIONARY.")
        word = input("Enter the word: ")
        meanings = input("Enter the meanings (separated by comma): ").split(',')
        self.dictionary.add_word(word, meanings)
        print(f"'{word}' added to dictionary.")

    def lookup_word(self):
        print("\nLOOK UP MEANING")
        word = input("Enter a word to look up: ")
        meanings = self.dictionary.lookup_word(word)
        if meanings:
            print(f"Meanings of '{word}': {', '.join(meanings)}")
        else:
            print(f"'{word}' not found in the dictionary.")
