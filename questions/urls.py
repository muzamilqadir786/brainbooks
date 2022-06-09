from django.urls import path
from django.views.generic import TemplateView

from . import views
urlpatterns = [
    path('free-mcqs/', views.free_mcqs_test, name='free_mcqs_test'),
    path('generate-paper/', views.generate_paper, name='generate_paper'),
    path('past-papers/', views.past_papers, name='past_papers'),
    path('ajax/load-dropdown/', views.load_dropdown_ajax, name='ajax_load_dropdown'),
    path('', views.generate_paper, name='index'),
]