import random
from django.db import models

# Create your models here.
BOARD_CHOICES = [
    ('PJ', 'Punjab'),
    ('SN', 'Sindh'),
    ('KP', 'Khyber Pakhtunkhwa'),
    ('BL', 'Balochistan'),
]
class Board(models.Model):
    board = models.CharField(
        max_length=2,
        choices=BOARD_CHOICES,
        unique = True,
        )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return dict(BOARD_CHOICES)[self.board]


CLASS_CHOICES = [
    ('9', 'Class-9'),
    ('10', 'Class-10'),
    ('11', 'Inter Part-I'),
    ('12', 'Inter Part-II'),
]

class Class(models.Model):
    # board = models.ForeignKey('Board', on_delete = models.CASCADE, blank=True, null=True)
    # board = models.ForeignKey('Board', on_delete = models.CASCADE, blank=True, null=True)
    boards = models.ManyToManyField('Board')
    board_class = models.CharField(
        max_length=2,
        choices=CLASS_CHOICES,
        default= '9',
    )

    def __str__(self):
        return dict(CLASS_CHOICES)[self.board_class] # + " " + self.board.__str__()

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Classes"
        # unique_together = ['board','board_class']

SUBJECT_CHOICES = [
    ('URD', 'Urdu'),
    ('ENG', 'English'),
    ('ISL', 'Islamiyat'),
    ('PHY', 'Physics'),
    ('CHE', 'Chemistry'),
    ('BIO', 'Biology'),
    ('MTM', 'Mathematics'),
    ('CMP', 'Computer'),
    ('STA', 'Statistics'),
    
]

class Subject(models.Model):
    # classes = models.ForeignKey('Class', on_delete=models.CASCADE, related_name='subjects', blank=True, null=True, verbose_name='Class')
    # classes = models.ManyToManyField('Class', related_name='subjects', blank=True, verbose_name='Class')
    subject = models.CharField(
        max_length=3,
        choices=SUBJECT_CHOICES,
        default= 'MIS',
        blank=True,
        unique = True
    )
    class Meta:
        # unique_together = ['subject', 'classes']
        ordering = ['id']

    def __str__(self):
        return dict(SUBJECT_CHOICES)[self.subject]

class SubjectClass(models.Model):
    subject_class = models.ForeignKey('Class', on_delete=models.CASCADE, verbose_name='Class', blank=True, null=True)
    subject_name = models.ForeignKey('Subject', on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Class Subjects'
        unique_together = ['subject_class', 'subject_name']

    def __str__(self):
        return '{} {}'.format(self.subject_name.subject, self.subject_class)

class Unit(models.Model):
    unit_subject = models.ForeignKey('Subject', on_delete=models.CASCADE, blank=True, null=True)
    unit_class = models.ForeignKey('Class', on_delete=models.CASCADE, blank=True, null=True)

    unit_number = models.CharField(
        choices = [(str(x), 'UNIT-{}'.format(x)) for x in list(range(1,31))],
        max_length = 3,
        verbose_name = 'Unit Number',
    )

    unit_name = models.CharField(
        max_length=100,
        unique = True,
        verbose_name = 'Unit Name',
    )

    def get_unit_subjects(self):
        return Unit.objects.get(id=self.id).unit_subject

    class Meta:
        unique_together = ['unit_subject', 'unit_number']

    def __str__(self):
        return 'UNIT-{} {}-'.format(self.unit_number, self.unit_name)

    # objects = models.Manager()

QUESTION_TYPES = (
    (1, 'MCQ'),
    (2, 'Short Question'),
    (3, 'Long Question'),
)


class Question(models.Model):
    unit=models.ForeignKey('Unit',on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def get_questions_by_unit(self, *args, **kwargs):
        unit = Unit.objects.get(unit_number=kwargs['unit_number'])
        questions = Question.objects.filter(unit=unit.unit_name)

    def __str__(self):
        return self.question