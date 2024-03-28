create_word_table_query = """
CREATE TABLE IF NOT EXISTS Word (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT UNIQUE NOT NULL
);
"""

create_definition_table_query = """
CREATE TABLE IF NOT EXISTS Definition (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id INTEGER NOT NULL,
    definition TEXT NOT NULL,
    part_of_speech TEXT,
    FOREIGN KEY (word_id) REFERENCES Word(id)
);
"""

