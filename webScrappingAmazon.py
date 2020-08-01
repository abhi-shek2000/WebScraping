from bs4 import BeautifulSoup
import requests
import csv

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

source = requests.get('https://www.amazon.in/s?k=Laptops&ref=nb_sb_noss_2', headers = headers).text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

Names = []
Prices = []

# for loop

for i in soup.find_all('a', class_='a-link-normal a-text-normal'):
    string = i.text
    Names.append( string.strip() )

for i in soup.find_all('span', class_='a-price-whole'):
    Prices.append(i.text)


file_name = 'Laptops.csv'

with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.No', 'Laptop Name', 'Prices'])

    for i in range(len(Names)):
        writer.writerow([i, Names[i], Prices[i]])


