# CLI Blank Dictionary

This is a command-line interface (CLI) project for a blank dictionary, where users can input words along with their meanings. The project utilizes Python and SQLite to store and manage the data. Users can also look up words to retrieve their meanings if they exist in the dictionary.

## Features

- Add new words along with their meanings.
- Look up existing words to retrieve their meanings.
- Data persistence using SQLite database.
- Simple and easy-to-use command-line interface.

## Prerequisites

Before running the program, ensure that you have the following installed:

- Python 3.x
- SQLite3 


## Usage

You will be presented with a menu to choose from:

1. Add a new word
2. Look up a word
3. Delete word
4. Update word
5. Exit

### Adding a New Word

To add a new word, select option 1 from the menu. You will be prompted to enter the word and its meaning. Once entered, the word and its meaning will be saved in the dictionary.

### Looking Up a Word

To look up a word, select option 2 from the menu. You will be prompted to enter the word you want to look up. If the word exists in the dictionary, its meaning will be displayed. If the word is not available, you will be notified that the word is not found.

### Deleting a word 
To delete a word select option 3 from the menu. You will be prompted to enter the word you want to eliminate from the dictionary. If the word exists in the dictionary it will be deleted and if not "word not found" will be printed out.

### Updating a word
To update a word select option 4 from the menu where you will be prompted to key in the word you want to update. You can update its meaning and even change the whole word completely.

### Exiting the Program

To exit the program, select option 3 from the menu.

## Database Structure

The database contains two tables:

1. `words`: Stores the words entered by the user.
2. `meanings`: Stores the meanings corresponding to the words entered.

The tables are linked by a foreign key constraint.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.
