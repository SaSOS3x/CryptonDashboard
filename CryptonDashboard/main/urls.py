from django.urls import path
from . import views
#from views import IndexDetailView

urlpatterns = [
    path('', views.main, name='home'),

    path('active', views.active),
    path('upcoming', views.upcoming),
    path('ended', views.ended),

    path('newest', views.newest),
    path('raiting', views.raiting),
    path('complexity', views.complexity),

    path('info/<node_name>', views.info, name='info'),

    path('info/<node_name>/<node_guide>', views.guide, name='info'),

    path('world/<node_name>', views.world),

]