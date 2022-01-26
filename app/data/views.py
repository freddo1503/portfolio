"""DOC"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from postgres.models import Ticker, News
import requests


PUBLIC_TOKEN='OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX'

def index(request):
    """Get default AAPL"""
    response = requests.get('https://eodhistoricaldata.com/api/news?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&s=AMZN.US&offset=0&limit=10')
    newsdata = response.json()
    print(Ticker.__str__)
    return render(request, 'news/index.html', {
        'title': newsdata[0]['title'],
        'content': newsdata[0]['content'],
        "tickers": Ticker.objects.all()
    })

@login_required
def get_day_news(request):
    """Select the data to add"""
    if request.method == "POST":
        selected_ticker = request.POST['ticker']
        response = requests.get(
            f'https://eodhistoricaldata.com/api/news?api_token={PUBLIC_TOKEN}&s={selected_ticker}.US&offset=0&limit=10')
        newsdata = response.json()

        add = News(
            title=newsdata[0]['title'],
            content=newsdata[0]['content'],
            date=newsdata[0]['date'],
            ticker=Ticker.objects.get(ticker=selected_ticker)
        )
        add.save()
    return render(request, 'news/index.html',{
            'date': newsdata[0]['date'],
            'title': newsdata[0]['title'],
            'content': newsdata[0]['content'],
            'selected_ticker':selected_ticker,
            "tickers": Ticker.objects.all()
    })
