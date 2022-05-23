from django.shortcuts import render
from lists.models import Item

def home_page(request):
    post_item_text = request.POST.get('item_text','')
    if post_item_text != '':
        item = Item()
        item.text = post_item_text
        item.save()
    return render(request,'home.html', {'new_item_text':post_item_text})
