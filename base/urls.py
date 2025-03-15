from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.test, name="test"),
    path("iata/", views.IATA, name="hard-roudemap"),
    path("go/", views.go_form, name="go-form"),
    path("go-and-come/", views.go_and_come_form, name="go-and-come-form"),
    path("hard-roudmap/", views.hard_roudemap_form, name="hard-roudemap"),
]
