from django.urls import path
from . import views
#from views import IndexDetailView

urlpatterns = [
    path('', views.info, name='info'),
]