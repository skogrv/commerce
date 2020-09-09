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
    path("listings", views.Listing.as_view(), name="listings"),
    path("mylistings", views.Listingmy.as_view(), name="mylistings")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




