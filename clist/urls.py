from django.urls import path
from . import views
app_name = 'clist'
urlpatterns = [path("", views.contact_list, name='contact_list'),
               path("<slug:slug>/", views.contact_detail, name='contact_detail')
               ]
