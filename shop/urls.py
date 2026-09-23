from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("api/status/", views.status, name="status"),
    path("admin-panel/", views.forbidden, name="forbidden"),
]