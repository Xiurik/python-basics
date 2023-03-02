import requests
from bs4 import BeautifulSoup
import pprint as pp
import time as t


def sort_stories(hnlist):
    return sorted(hnlist, key=lambda x: x["votes"], reverse=True)


def create_custom_hn(links, votes):
    hnl = []
    for idx, item in enumerate(links):
        score = votes[idx].select(".score")
        if len(score) == 0:
            continue

        cp = int(score[0].getText().replace(" points", ""))
        if cp > 10:
            title = item.getText()
            href = item.a["href"]
            hnl.append({"title": title, "link": href, "votes": cp})

    return sort_stories(hnl)


def load_data(amount):
    link = "http://news.ycombinator.com/news"
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.select(".titleline")
    votes = soup.select(".subtext")
    link_sources = []
    votes_sources = []

    if amount == 1:
        return create_custom_hn(links, votes)
    elif amount > 1:
        link_sources = link_sources + links
        votes_sources = votes_sources + votes
        for i in range(2, amount):
            res = requests.get(link + "?p=" + str(i))
            soup = BeautifulSoup(res.text, "html.parser")
            link_sources = link_sources + soup.select(".titleline")
            votes_sources = votes_sources + soup.select(".subtext")
            t.sleep(3)
        return create_custom_hn(link_sources, votes_sources)


pp.pprint(load_data(4))
