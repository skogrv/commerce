from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError
from .models import User, Auction
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from .forms import AuctionForm


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



class Listing(ListView):
    model = Auction
    template_name = 'auctions/listings.html'




class Listingmy(ListView):
    model = Auction
    template_name = 'auctions/mylistings.html'


