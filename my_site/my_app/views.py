from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page",
    "crypto": "Crypto Page"

}

def news_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 Generic Error")

def add_view(request, num1, num2):
    result = num1 + num2
    return HttpResponse(str(result))
