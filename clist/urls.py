from django.urls import path
from . import views
app_name = 'clist'
urlpatterns = [path("", views.contact_list, name='contact_list'),
               path("add_contact/", views.add_contact, name="add_contact"),
               path("<slug:slug>/", views.contact_detail, name='contact_detail'),
               ]
