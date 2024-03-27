import sqlite3

class Dictionary:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS words (
                                id INTEGER PRIMARY KEY,
                                word TEXT UNIQUE
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS meanings (  
                                id INTEGER PRIMARY KEY,
                                word_id INTEGER,
                                meaning TEXT,
                                FOREIGN KEY (word_id) REFERENCES words(id)
                            )''')
        self.connection.commit()

    def add_word(self, word, meanings):
        self.cursor.execute('''INSERT INTO words (word) VALUES (?)''', (word,))
        word_id = self.cursor.lastrowid

        for meaning in meanings:
            self.cursor.execute('''INSERT INTO meanings (word_id, meaning) VALUES (?, ?)''', (word_id, meaning))

        self.connection.commit()

    def lookup_word(self, word):
        self.cursor.execute('''SELECT meaning FROM meanings WHERE word_id = (SELECT id FROM words WHERE word = ?)''', (word,))
        meanings = self.cursor.fetchall()
        return [meaning[0] for meaning in meanings]
