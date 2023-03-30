from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ItemForm
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list,}
    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse('<h1>This is a item view.</h1><p>This is some test text for checking how it is working</p><h2>Working fine</h2>')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    context = {
        'form': form
    }
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', context)