from django.urls import path

from .views import profile, profile_update

app_name = "profile"

urlpatterns = [
    path("me/", profile, name="index"),
    path("edit/", profile_update, name="update"),
]
