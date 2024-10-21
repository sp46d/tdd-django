from django.shortcuts import redirect, render

from lists.models import Item, List


# Create your views here.
def home_page(request):
    return render(request, "lists/home.html")


def view_list(request, list_id: int):
    our_list = List.objects.get(id=list_id)
    return render(request, "lists/list.html", {"list": our_list})


def new_list(request):
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect(f"/lists/{nulist.id}/")


def add_item(request, list_id: int):
    existing_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["item_text"], list=existing_list)
    return redirect(f"/lists/{existing_list.id}/")


# How I would approach this to resolve the issue:
# 1. Now we need authentication system. We need to implement User model. NO NEED TO USE AUTHENTICATION
# 2. Associate different lists with different users. NO NEED TO INTRODUCE USERS JUST YET.
# 3. One to one relationship between list and user

# The approach the book is taking:
# 1. Implement functionality of adding an item to existing list (/lists/<list_id>/add_item).
