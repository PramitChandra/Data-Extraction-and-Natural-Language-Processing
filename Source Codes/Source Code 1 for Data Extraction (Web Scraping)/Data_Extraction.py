import requests
from bs4 import BeautifulSoup


url = " URL of the webpage you want to extract data from "
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

title_element = soup.find('h1')
if title_element is not None:
    title = title_element.text.strip()
else:
    title = "Title not found"


text_elements = soup.find_all('div', class_='tdb-block-inner td-fix-index')
text = '\n\n'.join([element.text.strip() for element in text_elements])

print("Article Title:")
print(title)
print("\nArticle Text:")
print(text)

