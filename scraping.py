import requests
import csv
from bs4 import BeautifulSoup

count = 0

url = 'https://editorial.rottentomatoes.com/guide/popular-movies/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for any HTTP errors

    soup = BeautifulSoup(response.content, 'html.parser')
    movies = soup.find_all('div', class_="row countdown-item")

    filename = 'trending_movies.csv'

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['Id', 'Movie', 'Year', 'Rating(%)'])

        for movie in movies:
            name = movie.find('div', class_="row countdown-item-title-bar").a.text
            score = movie.find('span', class_="tMeterScore").text.strip("%")
            year = movie.find('span', class_="subtle start-year").text.strip("()")
            count += 1

            writer.writerow([count, name, year, score])

    print(f'Movie data written to {filename} successfully.')
except Exception as e:
    print(e)
