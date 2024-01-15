from django.urls import include, path
from home.views import home_page

urlpatterns = [
    path('', home_page, name='home_page'),
]
