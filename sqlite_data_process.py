# import sqlite3
#
# # Connect to SQLite database (or any other DB)
# conn = sqlite3.connect('documents.db')
# cursor = conn.cursor()
#
# # Create reference documents table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS reference_documents (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     content TEXT NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )
# ''')
#
# # Create student documents table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS student_documents (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     student_id TEXT NOT NULL,
#     content TEXT NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )
# ''')
#
# conn.commit()
#################################
import requests
# from bs4 import BeautifulSoup
# import sqlite3
#
# # Connect to your database (if it's already created, otherwise create it)
# conn = sqlite3.connect('CapstoneV1.db')
# cursor = conn.cursor()

# # Create table for reference documents if it doesn't already exist
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS reference_documents (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     topic TEXT NOT NULL,
#     content TEXT NOT NULL
# )
# ''')
#
# Example website URL
# url = "https://www.cs.rit.edu/~hpb/Lectures/2221/605/605-81.html"  # Replace with your actual URL
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
#
# # Extract the title from the <a> tag with the specific name attribute
# title_tag = soup.find('a', {"name": "4.38. Calculate Sqrt(2) without the MathClass"})
# title = title_tag.text if title_tag else "Unknown Topic"
#
# # Extract the main content, ignoring images
# content = []
# for paragraph in soup.find_all(['p', 'pre']):  # Extract paragraphs and code blocks
#     if paragraph.find('img') is None:  # Skip any content with images
#         content.append(paragraph.get_text())
#
# # Combine the content into a single string
# content_text = "\n".join(content)
#
# # Insert the scraped title and content into the database
# cursor.execute('INSERT INTO reference_documents (topic, content) VALUES (?, ?)', (title, content_text))
#
# conn.commit()
# conn.close()
#
# print(f"Data successfully scraped and stored in the database with title: {title}")
####################
#STUDENT Document
# import sqlite3
#
# # Connect to your database (if it's already created, otherwise create it)
# conn = sqlite3.connect('CapstoneV1.db')
# cursor = conn.cursor()
#
# # Create table for student documents if it doesn't already exist
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS student_documents (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     topic TEXT NOT NULL,
#     content TEXT NOT NULL
# )
# ''')

# Student notes content
# student_topic = "Mixed Mode Arithmetic and Casting"
# student_notes = """
# Mixed Mode Arithmetic and Casting:
# - converted to the heaviest type (byte → char → short → int → l → f → d).
# - Example: 2 + 3.3 is interpreted as 2.0 + 3.3.
# - You can change the type using casting (place the target type in parentheses).
# - Example:
#   - aInt = 2 + (int) 3.3
#   - aInt = ?? (2 + 3.3)
#   - aDouble = 2 + 3.3
#
# Java Operators Example:
# - Example program dealing with operators:
#   - Outputs:
#     1. 'b'
#     2. 2
#     3. 2a (my assumption)
#     4. 20
#     5. b0
#     6. 1 (int division)
#     7. 2 (remainder)
#     8. 1 (casting double to int)
#     9. 1.04167 (double division)
#     10. 1.04167 (double division with 5.0)
# """
#
# # Insert student notes into the database
# cursor.execute('INSERT INTO student_documents (topic, content) VALUES (?, ?)', (student_topic, student_notes))
#
# # Commit the changes and close the connection
# conn.commit()
# conn.close()
#
# print("Student notes successfully inserted into the database.")



import sqlite3

# Connect to your database (if it's already created, otherwise create it)
conn = sqlite3.connect('CapstoneV1.db')
cursor = conn.cursor()

# Create table for student documents if it doesn't already exist
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS student_documents (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     topic TEXT NOT NULL,
#     content TEXT NOT NULL
# )
# ''')

# Student notes content (wrong code version)
student_id = 2
student_topic = "Pattern Matching"
student_notes = """

      
"a+b*" -> True
"x[a-z]+b" -> False
"^a[a-z][b-z]" -> False
"a*b*c*." -> True
"[0-9]{3}t[0-9]{2}" -> False
"[0-9]{3}\.[0-9]{2}" -> False
"""
#  # "\s\S\w" -> False; "^a[a-z][b-z]i" -> False
# Insert student notes into the database
cursor.execute('INSERT INTO student_documents (topic, content, studentid) VALUES (?, ?, ?)', (student_topic, student_notes, student_id))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Student notes with wrong code successfully inserted into the database.")
