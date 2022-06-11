from django.shortcuts import render
from .models import Board, Class, Subject, Chapter
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

def home(request):
    return render(request,'questions/home.html')

def free_mcqs_test(request):
    return render(request, 'questions/free_mcqs_test_page.html')

def past_papers(request):
    return render(request, 'questions/past_papers_page.html')

@login_required()
def generate_paper(request):
    context = {}
    context['boards'], context['classes'] = Board.objects.all(), Class.objects.all()
    context['subjects'], context['chapter']  =  Subject.objects.all(), Chapter.objects.all()
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
            # chapters_topics = [chapter.topic_set.all() for chapter in chapters]
            context['chapters'] = [{'name':unescape(str(chapter)),
                                    'chapter_id': chapter.chapter_id} for chapter in chapters]


                                    # 'chapter_topics': chapter.topic_set.all()
        return JsonResponse({'context':context})
        # HttpResponse(classes)
    # ipdb.set_trace()


"""
https://brainbooks.pk/api/filp_question/?request_type=flip_question&subject=56&cqid=Ques_LQ_80501&qid=80501&class_id=3&type=LQ&subshort=Story


https://brainbooks.pk/api/filp_question/?request_type=flip_question&subject=56&cqid=Ques_LQ_86033&qid=85965&class_id=3&type=LQ&subshort=Punctuation-BK1
https://brainbooks.pk/api/filp_question/?request_type=flip_question&subject=57&cqid=Ques_LQ_86033&qid=85965&class_id=3&type=LQ&subshort=MCQs-???,???- ?????,??? - ?????
"""

"""
https://brainbooks.pk/api/filp_question/?request_type=flip_question&subject=74&cqid=Ques_MCQS_80784&qid=80784&class_id=4&units=704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,747,720,&topics=3100,3101,3057,3058,3059,3060,&type=MCQS&subshort=MCQs-Correct-Meaning-BK-II(P-I)

"""

"""
https://brainbooks.pk/api/getreplactchapter/?board_id=1&class_id=3&subject_id=57&paper_medium=undefined&selectedUnits=441%2C442%2C443%2C444%2C445%2C447%2C446%2C448%2C449%2C450%2C451%2C452%2C453%2C454%2C455%2C456%2C457%2C458%2C459%2C460%2C461%2C462%2C463%2C464%2C465%2C466%2C467%2C468%2C1107%2C469%2C1108%2C470%2C1109%2C471%2C1110%2C472%2C1113%2C473%2C1112%2C474%2C1114%2C514%2C&paper_format=221&selectedtopics=2603%2C2744%2C2745%2C2758%2C2759%2C2760%2C2761%2C&with_pairing_scheme=0&question_medium_1=undefined&question_medium_2=undefined&question_medium_3=undefined&bubble_sheet=2&question_type=3%2C2%2C1%2C0&bypasserror=0&question_status=2&get_subject=1

"""