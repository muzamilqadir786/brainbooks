from django.contrib import admin
from .models import Board, Class , Subject, Chapter#, SubjectClass, Unit, Question
# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id','__str__']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id','__str__', 'board_name','status','icon']
    def board_name(self,obj):
        return obj.board.__str__()

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
    list_display = ['id', 'subject_id', 'board', 'class_name','__str__', 'get_subject', 'chapter', 'title', 'status']
    def get_subject(self, obj):
        return obj.subject.name
    def class_name(self,obj):
        return obj.class_name
    get_subject.short_description = 'Subject Name'
    class_name.short_description = 'Class Name'
    # get_author.admin_order_field = 'book__author'


# @admin.register(SubjectClass)
# class SubjectClassAdmin(admin.ModelAdmin):
#     list_display = ['subject_class', 'subject_name']
#
# @admin.register(Unit)
# class UnitAdmin(admin.ModelAdmin):
#     # list_display = [str(field.name) for field in Unit._meta.get_fields()]
#     list_display=['unit_number','unit_name','get_unit_subjects']
#     list_filter=['unit_name', 'unit_number']
#     search_fields=['unit_number','unit_name']
#     # def unit_class(self, obj,):
#
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Question._meta.get_fields()]


admin.site.site_header = "Question Bank Administration"
admin.site.site_title = "QUESTION BANK"
admin.site.index_title = "Welcome To: A Complete Academic Solution"


# admin.site.register(Board, BoardAdmin)
# admin.site.register(Class, ClassAdmin)
# admin.site.register(Subject, SubjectAdmin)
# admin.site.register(SubjectClass, SubjectClassAdmin)
# admin.site.register(Unit, UnitAdmin)
# admin.site.register(Question, QuestionAdmin)