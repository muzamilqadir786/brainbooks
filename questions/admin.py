from django.contrib import admin
from .models import Board, Class, Subject, Chapter, Topic, Question
# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id','__str__']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id','__str__', 'board_name','status','icon']
    def board_name(self,obj):
        return obj.board.__str__()
    # def get_queryset(self, request):
    #     queryset = super(ChapterAdmin, self).get_queryset(request).all(*args, **kwargs)
    #     queryset = queryset.prefetch_related('subject').all()
    #     return queryset

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject_id', 'board_name', 'class_name','__str__', 'total_type_questions', 'status', 'icon']
    # filter_horizontal = ('classes',)
    list_filter = ['class_name__name', 'subject_id']
    search_fields=['subject_id','class_name__name','board_name']
    def board_name(self,obj):
        return obj.board.__str__()
    def class_name(self,obj):
        return obj.class_name

import ipdb
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject_id', 'board', 'class_name','__str__', 'get_subject', 'chapter', 'chapter_id', 'title', 'status']
    list_filter = ['subject_id','subject__name']
    def get_subject(self, obj):
        return obj.subject.name
    def class_name(self,obj):
        return obj.class_name

    # def get_queryset(self, request):
    #     queryset = super(ChapterAdmin, self).get_queryset(request)
    #     queryset = queryset.prefetch_related('class').all()
    #     return queryset
    #     # ipdb.set_trace()
        # if request.user.is_superuser:
        #     return qs
        # return qs.filter(author=request.user)

    get_subject.short_description = 'Subject Name'
    class_name.short_description = 'Class Name'
    # get_author.admin_order_field = 'book__author'

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic_id', 'subject_id', 'board', 'class_name', 'subject', 'chapter', 'title', 'topic',  'status']
    # list_display = ['topic_id', 'subject_id', 'board', 'class_name', 'topic', 'title', 'status']
    list_filter = ['subject_id','subject__name']
    search_fields = ['topic_id', 'subject__name']

    def subject(self, obj):
        return obj.subject.__str__()

    def class_name(self,obj):
        return obj.class_name

    def chapter(self, obj):
        return obj.chapter.__str__()


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.get_fields()]
    list_display = ['topic_id', 'board','__str__', 'subject', 'chapter', 'topic', 'type','option1', 'option2', 'option3', 'option4', 'answer']
    # list_display = ['topic_id', 'subject_id', 'board', 'class_name', 'topic', 'title', 'status']
    list_filter = ['subject_id','subject__name']
    def subject(self, obj):
        return obj.subject.__str__()
    def chapter(self, obj):
        return obj.chapter.__str__()
    def topic(self, obj):
        return obj.topic.__str__()

admin.site.site_header = "Question Bank Administration"
admin.site.site_title = "QUESTION BANK"
admin.site.index_title = "Welcome To: A Complete Academic Solution"



