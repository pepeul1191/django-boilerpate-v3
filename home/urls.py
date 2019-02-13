from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'rest$', views.index_rest, name='index_rest'),
  url(r'^$', views.index_view, name='home_index'),
]
