from django.conf.urls import url
from django.urls import path

from mailing_hb import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
]