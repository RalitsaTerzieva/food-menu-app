from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ItemForm
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list,}
    return render(request, 'food/index.html', context)

class ListClassView(ListView):
    item = Item
    queryset = Item.objects.all()
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def item(request):
    return HttpResponse('<h1>This is a item view.</h1><p>This is some test text for checking how it is working</p><h2>Working fine</h2>')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)

class DetailClassView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    

def create_item(request):
    form = ItemForm(request.POST or None)
    context = {
        'form': form
    }
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', context)

class CreateItem(CreateView):
    model = Item;
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html';
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        
        return super().form_valid(form)

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    context = {
        'form': form,
        'item': item
    }
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', context)

def delete_item(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item': item
    }
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', context)