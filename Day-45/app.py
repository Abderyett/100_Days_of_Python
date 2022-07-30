from bs4 import BeautifulSoup


with open('./website.html') as file:
    contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.string)
# print(soup.title.name)
print(soup.prettify())
