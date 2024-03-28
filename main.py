from dictionary import Dictionary  # Import the Dictionary class from the dictionary module
class Interphase:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Add a new word")
            print("2. Look up a word")
            print("3. Delete word")
            print("4. Update word")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_word()
            elif choice == '2':
                self.lookup_word()
            elif choice == '3':
                self.delete_word()
            elif choice == '4':
                self.update_word()
            elif choice == '5':
                print("\nExiting the program. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number from 1 to 5.")

    def add_word(self):
        print("\nADD WORD TO DICTIONARY.")
        word_text = input("Enter the word: ")
        meanings = input("Enter the meanings (separated by comma): ").split(',')
        self.dictionary.add_word(word_text, meanings)
        print(f"'{word_text}' added to dictionary.")

    def lookup_word(self):
        print("\nLOOK UP MEANING")
        word_text = input("Enter a word to look up: ")
        meanings = self.dictionary.lookup_word(word_text)
        if meanings:
            print(f"Meanings of '{word_text}': {', '.join(meanings)}")
        else:
            print(f"'{word_text}' not found in the dictionary.")

    def delete_word(self):
        print("\nDELETE WORD FROM DICTIONARY.")
        word_text = input("Enter the word to delete: ")
        self.dictionary.delete_word(word_text)

    def update_word(self):
        print("\nUPDATE WORD IN DICTIONARY.")
        old_word_text = input("Enter the word to update: ")
        new_word_text = input("Enter the new word: ")
        new_meanings = input("Enter the new meanings (separated by comma): ").split(',')
        self.dictionary.update_word(old_word_text, new_word_text, new_meanings)

def main():
    dictionary = Dictionary('dictionary.db')
    interphase = Interphase(dictionary)
    interphase.run()
    dictionary.close_connection()

if __name__ == "__main__":
    main()
