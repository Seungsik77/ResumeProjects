from newspaper import Article
import requests
from bs4 import BeautifulSoup

def scrape_single_article(url):
    try:
        # newspaper3k method used for article extraction
        article = Article(url)
        article.download()
        article.parse()
        
        return {
            'title': article.title,
            'author': article.authors,
            'text': article.text,
            'url': url
        }
    except Exception as e:
        print(f"Failed with newspaper3k: {e}")
        # Fallback to BeautifulSoup
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            title = soup.find('h1', class_='article-title').text.strip() if soup.find('h1', class_='article-title') else ''
            content_div = soup.find('div', class_='article-content')
            text = '\n'.join([p.text.strip() for p in content_div.find_all('p')]) if content_div else ''
            
            return {
                'title': title,
                'author': [],
                'text': text,
                'url': url
            }
        except Exception as e:
            print(f"Fallback also failed: {e}")
            return None

# Test
article_url = input("Enter article URL: ") #input article URL here for testing
article = scrape_single_article(article_url)

if article:
    print(f'Title: {article["title"]}')
    print(f'Author: {article["author"]}')
    print(f'Text: {article["text"][:]}...')
    print(f'URL: {article["url"]}')
else:
    print("Failed to scrape article")