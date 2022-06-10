import random
import json
import requests
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
PUNJAB = 1
SINDH = 2
KHYBER_PAKHTUNKHWA = 3
BLOCHISTAN = 4
BOARD_CHOICES = [
    (PUNJAB, 'Punjab'),
    (SINDH, 'Sindh'),
    (KHYBER_PAKHTUNKHWA, 'Khyber Pakhtunkhwa'),
    (BLOCHISTAN, 'Balochistan'),
]
class Board(models.Model):
    name = models.CharField(
        max_length=1,
        choices=BOARD_CHOICES,
        unique = True,
        )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return dict(BOARD_CHOICES)[int(self.name)]

    @staticmethod
    def insert_data():
        for board in dict(BOARD_CHOICES).keys():
            # import ipdb
            # ipdb.set_trace()
            board_obj, created = Board.objects.get_or_create(name=board,id=board)
            if created:
                print("Created board with id:{}".format(board))
            else:
                print("Board already exists")
#Only change to push
NINTH = 1
TENTH = 2
FIRST_YEAR = 3
SECOND_YEAR = 4
CLASS_CHOICES = [
    (NINTH, 'Class-9'),
    (TENTH, 'Class-10'),
    (FIRST_YEAR, 'Inter Part-I'),
    (SECOND_YEAR, 'Inter Part-II'),
]

class Class(models.Model):
    board = models.ForeignKey('Board', blank=True, null=True, on_delete=models.CASCADE)
    name = models.PositiveSmallIntegerField(
        choices=CLASS_CHOICES,
        # db_column = 'class',
    )

    status = models.BooleanField(default=True)
    icon = models.ImageField(upload_to ='icons/', blank=True)
    def __str__(self):
        return dict(CLASS_CHOICES)[self.name]

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Classes"
        unique_together = ['board','name']

    def class_subjects(self):
        return self.subject_set.all()

    def get_queryset(self):
        return self.subject_set.all()

    @staticmethod
    def insert_data():
        board_obj, created = Board.objects.get_or_create(name=PUNJAB)
        for key,value in dict(CLASS_CHOICES).items():
            obj, created = Class.objects.get_or_create(name=key,board=board_obj,id=key)
            if created:
                print("Class Object created with class {} created successfully.".format(key))
            else:
                print("Class Object already exists")

class Subject(models.Model):
    subject_id = models.PositiveIntegerField(blank=True, null=True)
    board = models.ForeignKey('Board', blank=True, null=True, on_delete=models.CASCADE)
    class_name = models.ForeignKey('Class', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100,
        blank=True,
        unique = True
    )
    total_type_questions = models.PositiveSmallIntegerField(blank=True, null=True)
    status = models.BooleanField(default=True)
    icon = models.ImageField(upload_to ='icons/', blank=True)

    class Meta:
        unique_together = ['name', 'class_name']
        ordering = ['id']

    def __str__(self):
        return self.name


class Chapter(models.Model):
    chapter_id = models.PositiveSmallIntegerField(blank=True, null=True)
    board = models.ForeignKey('Board', blank=True, null=True, on_delete=models.CASCADE)
    class_name = models.ForeignKey('Class', blank=True, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', blank=True, null=True, on_delete=models.CASCADE)
    chapter = models.PositiveSmallIntegerField(blank=True, null=True) #This is the chapter number like U1, U2
    title = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'U-{self.chapter} {self.title}'

    def get_queryset(self):
        return super().get_queryset().filter(class_name=self.class_name)
        # return self.subject_set.all()

    class Meta:
        unique_together = ['chapter', 'chapter_id']
        ordering = ['id']
        


import ipdb
class Topic(models.Model):
    topic_id = models.PositiveSmallIntegerField(blank=True, null=True)
    board = models.ForeignKey('Board', blank=True, null=True, on_delete=models.CASCADE)
    class_name = models.ForeignKey('Class', blank=True, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', blank=True, null=True, on_delete=models.CASCADE)
    chapter = models.ForeignKey('Chapter', blank=True, null=True, on_delete=models.CASCADE)
    topic = models.CharField(max_length=10,blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['topic_id','title']
        ordering = ['subject_id','topic']

QUESTION_TYPES = (
    (1, 'MCQ'),
    (2, 'Short Question'),
    (3, 'Long Question'),
)

OPTION_A = 1
OPTION_B = 2
OPTION_C = 3
OPTION_D = 4

ANSWER_OPTIONS=(
    (OPTION_A,'Option1'),
    (OPTION_B,'Option2'),
    (OPTION_C,'Option3'),
    (OPTION_D,'Option4')
)

class Question(models.Model):
    board = models.ForeignKey('Board', blank=True, null=True, on_delete=models.CASCADE)
    class_name = models.ForeignKey('Class', blank=True, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', blank=True, null=True, on_delete=models.CASCADE)
    chapter = models.ForeignKey('Chapter', blank=True, null=True, on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', blank=True, null=True, on_delete=models.CASCADE)

    type = models.PositiveSmallIntegerField(choices=QUESTION_TYPES, blank=True, null=True)
    marks=models.PositiveSmallIntegerField()
    question=models.CharField(max_length=600, blank=True, null=True)
    option1=models.CharField(max_length=200, blank=True, null=True)
    option2=models.CharField(max_length=200, blank=True, null=True)
    option3=models.CharField(max_length=200, blank=True, null=True)
    option4=models.CharField(max_length=200, blank=True, null=True)

    answer = models.PositiveSmallIntegerField(choices=ANSWER_OPTIONS, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default=True)

    def get_questions_by_unit(self, *args, **kwargs):
        unit = Chapter.objects.get(unit_number=kwargs['unit_number'])
        questions = unit.question_set.all()


    def __str__(self):
        return self.question
