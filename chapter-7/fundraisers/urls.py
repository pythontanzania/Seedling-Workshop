from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("fundraiser/<int:fundraiser_id>/", views.fundraiser_detail, name="fundraiser_detail"),
    path("fundraiser/<int:fundraiser_id>/pledge/", views.pledge_create, name="pledge_create"),
    path("pledge/<int:pledge_id>/lipa/", views.lipa, name="lipa"),
    path("pledge/<int:pledge_id>/callback/", views.payment_callback, name="payment_callback"),
    path("manage/", views.manage, name="manage"),
    path("manage/new/", views.fundraiser_create, name="fundraiser_create"),
]
