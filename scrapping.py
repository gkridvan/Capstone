import requests
import csv
import time

def write_to_csv(articles, filename='articles.csv'):
    headers = ['ID', 'Slug', 'Title', 'Summary', 'Published From', 'Image URL', 'Reading Time']
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers) 
        for article in articles:
            writer.writerow(article)  

def fetch_page_data(page_number):
    url = f"https://bff-service.rtbf.be/oaos/v1.5/pages/en-continu?_page={page_number}&_limit=20"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching page {page_number}: {response.status_code}")
        return None

def extract_articles(data):
    articles = []
    
    for article in data['data']['articles']:
        article_info = [
            article['id'],
            article['slug'],
            article['title'],
            article['summary'],
            article['publishedFrom'],
            article['image']['illustration']['l'],  
            article['readingTime']
        ]
        articles.append(article_info)
    
    return articles

page_number = 1
all_articles = []

while page_number < 100:
    data = fetch_page_data(page_number)
    
    if data is None or not data['data']['articles']:
        break
    
    articles = extract_articles(data)
    all_articles.extend(articles)
    
    if data['links']['next']:
        page_number += 1
    else:
        break
    
    time.sleep(1)

write_to_csv(all_articles)
