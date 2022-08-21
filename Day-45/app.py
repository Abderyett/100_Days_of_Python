from distutils.filelist import findall
from bs4 import BeautifulSoup


with open('./website.html') as file:
    contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.string)
# print(soup.title.name)
# print(soup.prettify())

all_anchers_tags = soup.find_all(name="a")

for tag in all_anchers_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

header = soup.find(name='h1', id='name')

# print(header)

h3_heading = soup.find_all(name='h3', class_='heading')

print(h3_heading)

name = soup.select_one('#name')

print(name)

headings = soup.select('.heading')

print(headings)
