from lib.dictionary import Dictionary
from lib.cli import Interphase

def main():
    dictionary = Dictionary('dictionary.db')
    interphase = Interphase(dictionary)
    interphase.run()
    dictionary.close_connection()

if __name__ == "__main__":
    main()
