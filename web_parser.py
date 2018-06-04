from lxml import html
import requests
import requests_cache
import yaml

RULES_YML_URL = 'https://raw.githubusercontent.com/github/choosealicense.com/gh-pages/_data/rules.yml'

LICENSE_TABLE_URL = 'https://choosealicense.com/appendix/'
LICENSE_BASE_URL = 'https://raw.githubusercontent.com/github/choosealicense.com/gh-pages/_licenses/'

requests_cache.install_cache('api-cache', expire_after=86400)


def get_license(id, slim=True):
    url = LICENSE_BASE_URL + id + '.txt'
    page = requests.get(url)
    _, yml, text = page.text.split('---', 2)
    yml = yaml.load(yml)
    yml['id'] = id
    if not slim:
        yml['text'] = text.strip()
    return yml


def get_rules():
    text = requests.get(RULES_YML_URL).text
    return yaml.load(text)


def get_licenses():
    page = requests.get(LICENSE_TABLE_URL)
    tree = html.fromstring(page.content)
    return [
        {
            k: v
            for k, v in get_license(href_parts[2]).items()
            if k in {
                'id',
                'source',
                'permissions',
                'conditions',
                'limitations',
                'nickname',
                'description',
            }
        }
        for href_parts in (
            href.split('/')
            for href in tree.xpath('//@href')
        )
        if len(href_parts) > 2 and href_parts[1] == 'licenses'
    ]
