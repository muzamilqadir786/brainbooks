from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='main-index'),
    path('generate_paper/', views.generate_paper, name='paper-generator'),
]