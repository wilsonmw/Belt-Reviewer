from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^books$', views.index),
    url(r'^addPage$', views.addPage),
    url(r'^addBook$', views.addBook),
    url(r'^addReview$', views.addReview),
    url(r'^review$', views.review),
]