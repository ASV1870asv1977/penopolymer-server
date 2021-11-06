from django import template
import requests
from bs4 import BeautifulSoup as BS

from penopolimer_v2.settings.base import HEADERS, DOMAIN


register = template.Library()


@register.simple_tag
def get_parse(url_page, **kwargs):
    url = DOMAIN + str(url_page)
    search_query = kwargs['search']

    response = requests.get(url, headers=HEADERS)
    soup = BS(response.text, 'html')
    body_text = soup.find('body')

    text = body_text.text.lower()

    if search_query in text:
        return True
