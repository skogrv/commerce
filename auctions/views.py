from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from .models import User, Auction
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from .forms import AuctionForm
from cart.cart import Cart
from rest_framework.views import APIView


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "not valid"
            })
    return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return render(request, "auctions/login.html", {
        "message": "you have logged out"
    })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


class CreateListing(CreateView):
    model = Auction
    form_class = AuctionForm
    template_name = 'auctions/create_listing.html'


class Listings(ListView):
    model = Auction
    template_name = 'auctions/listings.html'


class Listingmy(ListView):
    model = Auction
    template_name = 'auctions/mylistings.html'


class EditPost(UpdateView):
    model = Auction
    form_class = AuctionForm
    template_name = 'auctions/edit_post.html'


class DeletePost(DeleteView):
    model = Auction
    template_name = 'auctions/delete_post.html'
    success_url = reverse_lazy('mylistings')


class CheckPost(DetailView):
    model = Auction
    template_name = 'auctions/listing.html'


def watchlist(request):
    return render(request, "auctions/watchlist.html", {"user": User})


def add_fav(request, id):
    cart = Cart(request)
    post = Auction.objects.get(id=id)
    cart.add(product=post)
    return redirect("watchlist")


def item_clear(request, id):
    cart = Cart(request)
    product = Auction.objects.get(id=id)
    cart.remove(product)
    return redirect("watchlist")

def items_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("watchlist")
