from django.conf.urls.static import static
from django.urls import path

from . import views
from commerce import settings


urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.CreateListing.as_view(), name="create_listing"),
    path("create_listing", views.CreateListing.as_view(), name="create_listing"),
    path("listings", views.Listings.as_view(), name="listings"),
    path("mylistings", views.Listingmy.as_view(), name="mylistings"),
    path("edit<int:pk>", views.EditPost.as_view(), name="edit"),
    path("delete<int:pk>", views.DeletePost.as_view(), name="delete"),
    path("listing<int:pk>", views.CheckPost.as_view(), name="listing"),
    path("fav_add<int:id>", views.add_fav, name="add_fav"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("remove<int:id>", views.item_clear, name="remove_fav"),
    path("clear_card", views.items_clear, name="cart_clear"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




