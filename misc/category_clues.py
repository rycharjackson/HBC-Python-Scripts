# Goal
# Print the value, question, and answer for Jeopardy clues from a
# random category

# SQL to get a random game:
# SELECT id, name FROM category ORDER BY RANDOM() LIMIT 1

# SQL to select the value, question, and answer for Jeopardy clues
# from a particular category:
# """SELECT text, answer, value FROM clue
#    WHERE game=%d ORDER BY value""" % (category_id,)
import sqlite3

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

# Get a random game.
cursor.execute("SELECT id, name FROM category ORDER BY RANDOM() LIMIT 1")
results = cursor.fetchall()

category_id, name = results[0]
print(name)

# Get and print the clues for our random category.
query = """SELECT text, answer, value FROM clue 
WHERE category=%s ORDER BY value""" % (category_id,)
cursor.execute(query)
results = cursor.fetchall()


# TODO: process results.
for clue in results:
    text, answer, value = clue
    print("[$%s]" % (value,))
    print("Question: %s" % (text,))
    print("Answer: What is '%s'?" % (answer,))
    print("")

connection.close()