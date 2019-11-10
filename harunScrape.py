
#blog post scraper
import bs4, requests
site = requests.get('http://harunaadoga.github.io')
site.raise_for_status
siteSoup = bs4.BeautifulSoup(site.text, "html.parser")
data = siteSoup.select('#blog')
print(data[0].getText())
