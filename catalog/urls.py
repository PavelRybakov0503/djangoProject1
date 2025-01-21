from django.urls import path, include
from django.utils.translation.trans_real import catalog

from catalog.apps import CatalogConfig
from catalog.views import home_view, contacts_view

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home_view, name='home'),
    path('contact/', contacts_view, name='contact'),
]
