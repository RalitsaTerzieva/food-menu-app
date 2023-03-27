from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

# Create your views here.
def index(requst):
    item_list = Item.objects.all()
    return HttpResponse(item_list)


def item(request):
    return HttpResponse('<h1>This is a item view.</h1><p>This is some test text for checking how it is working</p><h2>Working fine</h2>')