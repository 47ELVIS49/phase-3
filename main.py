from dictionary import Dictionary
from cli import CLI

def main():
    dictionary = Dictionary('dictionary.db')
    cli = CLI(dictionary)
    cli.run()

if __name__ == "__main__":
    main()
