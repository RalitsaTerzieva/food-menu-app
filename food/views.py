from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {'item_list': item_list,}
    return HttpResponse(template.render(context, request))


def item(request):
    return HttpResponse('<h1>This is a item view.</h1><p>This is some test text for checking how it is working</p><h2>Working fine</h2>')