from django.shortcuts import render, redirect, HttpResponse
from ..logreg.models import User
from .models import Item
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def dashboard(request):
    if 'username' not in request.session['user']:
        return redirect('logreg:index')
    user = User.objects.get(id=request.session['user']['id'])
    context = {
        'added_items': Item.objects.filter(added_by=user).exclude(user=user),
        'all_items': Item.objects.all(),
        'my_items': Item.objects.filter(user=user),
        'all_users': User.objects.exclude(id=user.id).order_by('username')
    }
    return render(request, "wishlist/dashboard.html", context)


def add_item(request):
    return render(request, "wishlist/add_item.html")


def submit_item(request):
    user = User.objects.get(id=request.session['user']['id'])
    results = Item.objects.validate_item(request.POST)
    if len(results) < 1:
        item = Item.objects.create_item(request.POST)
        item.added_by.add(user)
        return redirect("wishlist:dashboard")
    else:
        for error in results:
            messages.error(request, error)
        return redirect('wishlist:add_item')


def show(request, item_id):
    item = Item.objects.filter(id=item_id)
    context = {
        'item': item,
    }
    return render(request, "wishlist/show.html", context)


def profile(request, item_user_id):
    user = User.objects.get(id=item_user_id)
    current_user = request.session['user']['id']
    context = {
        'user': user,
        'items': Item.objects.filter(added_by=user),
        'my_items': Item.objects.filter(user=current_user),
        'added_items': Item.objects.filter(added_by=current_user)
    }
    return render(request, "wishlist/profile.html", context)


def join(request, item_id):
    Item.objects.join(item_id, request.session['user']['id'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'wishlist:dashboard'))


def unjoin(request, item_id):
    user = User.objects.get(id=request.session['user']['id'])
    item = Item.objects.get(id=item_id)
    item.added_by.remove(user)
    item.save()
    return redirect("wishlist:dashboard")


def delete(request, item_id):
    Item.objects.get(id=item_id).delete()
    return redirect("wishlist:dashboard")


