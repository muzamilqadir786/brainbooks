from django.shortcuts import render
from .models import Board, Class, Subject
# Create your views here.

def index(request):
    boards = Board.objects.all()
    classes = Class.objects.all()
    subjects = Subject.objects.all()
    context = {}
    context['boards'] = boards
    context['classes'] = classes
    context['subjects'] = subjects
    # import ipdb
    # ipdb.set_trace()
    # print("here in index view")

    return render(request,'questions/index.html',context)

def generate_paper(request):
    context = {}
    return render(request,'questions/generate_paper.html', context)