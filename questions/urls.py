from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('generate_paper/', views.generate_paper, name='generate_paper'),
    path('ajax/load-dropdown/', views.load_dropdown_ajax, name='ajax_load_dropdown'),
]