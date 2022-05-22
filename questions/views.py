from django.shortcuts import render
from .models import Board, Class, Subject, Chapter
from django.shortcuts import get_object_or_404
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
def index(request):
    boards = Board.objects.all()
    classes = Class.objects.all()
    # subjects = Subject.objects.all()
    context = {}
    context['boards'] = boards
    context['classes'] = classes
    # context['subjects'] = subjects
    # import ipdb
    # ipdb.set_trace()
    # print("here in index view")

    return render(request,'questions/index.html',context)

def generate_paper(request):
    context = {}
    context['boards'] = Board.objects.all()
    context['classes'] = Class.objects.all()
    context['subjects'] = Subject.objects.all()
    context['chapter'] = Chapter.objects.all()
    return render(request,'questions/generate_paper.html', context)

import ipdb
from django.utils.safestring import mark_safe
from django.utils.html import escape
from html import unescape
@csrf_exempt
def load_dropdown_ajax(request):
    if request.method == 'POST':
        context = {}
        board_id = request.POST.get('board_id')
        if board_id:
            board = get_object_or_404(Board, id=board_id)
            classes = board.class_set.all()
            context['classes'] = [{'name':str(cls),'id':cls.id} for cls in classes]

        class_id = request.POST.get('class_id')
        if class_id:
            class_obj = get_object_or_404(Class, id=class_id)
            subjects = class_obj.subject_set.all()
            context['subjects'] = [{'name':subject.name, 'subject_id':subject.subject_id} for subject in subjects]

        subject_id = request.POST.get('subject_id')
        if subject_id:
            subject = get_object_or_404(Subject, subject_id=subject_id)
            chapters = subject.chapter_set.all()
            context['chapters'] = [{'name':unescape(str(chapter)), 'chapter_id': chapter.chapter_id} for chapter in chapters]

        return JsonResponse({'context':context})
        # HttpResponse(classes)
    # ipdb.set_trace()

