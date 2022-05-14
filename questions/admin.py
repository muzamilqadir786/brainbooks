from django.contrib import admin
from .models import Board, Class, Subject, SubjectClass, Unit, Question
# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id','board']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id','__str__']
    # list_display = [field.name for field in Board._meta.get_fields()]
    def boards(self,obj):
        return obj.board

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','__str__']
    # list_display = [field.name for field in Subject._meta.get_fields()]
    # filter_horizontal = ('classes',)

@admin.register(SubjectClass)
class SubjectClassAdmin(admin.ModelAdmin):
    list_display = ['subject_class', 'subject_name']

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    # list_display = [str(field.name) for field in Unit._meta.get_fields()]
    list_display=['unit_number','unit_name','get_unit_subjects']
    list_filter=['unit_name', 'unit_number']
    search_fields=['unit_number','unit_name']
    # def unit_class(self, obj,):

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