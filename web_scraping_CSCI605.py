import requests
from bs4 import BeautifulSoup
import sqlite3

# Connect to your database
conn = sqlite3.connect('CapstoneV1.db')
cursor = conn.cursor()
#
# # Example website URL (replace with your target URL)
# url = "https://www.cs.rit.edu/~hpb/Lectures/2221/605/605-81.html#4.38.%20Calculate%20Sqrt(2)%20without%20the%20MathClass"  # Replace this with your actual URL
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# topic = "Calculate Sqrt"
# # Assuming the documents are inside <p> tags or a specific class
# documents_ref = ""
# # print(documents_ref)
# for paragraph in soup.find_all('p'):  # Modify based on your HTML structure
#     documents_ref += "\n" + paragraph.get_text()
# print(documents_ref)
# # Insert scraped data into the database
# # for doc in documents_ref:
# cursor.execute('INSERT INTO reference_documents (content, topic) VALUES (?, ?)', (documents_ref, topic))
#
# conn.commit()
# conn.close()


# Example website URL
url = "https://www.cs.rit.edu/~hpb/Lectures/2221/605/605-104.html"  # Replace with your actual URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title from the <a> tag with the specific name attribute
title_tag = soup.find('a', {"name": "4.38. Calculate Sqrt(2) without the MathClass"})
title = title_tag.text if title_tag else "Unknown Topic"
title = "Patterns"
# Extract the main content, ignoring images
content = []
for paragraph in soup.find_all(['p', 'pre']):  # Extract paragraphs and code blocks
    if paragraph.find('img') is None:  # Skip any content with images
        content.append(paragraph.get_text())

# Combine the content into a single string
content_text = "\n".join(content)

# Insert the scraped title and content into the database
cursor.execute('INSERT INTO reference_documents (topic, content) VALUES (?, ?)', (title, content_text))

conn.commit()
conn.close()

