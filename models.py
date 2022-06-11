# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ContactContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'contact_contact'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoFlatpage(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    enable_comments = models.BooleanField()
    template_name = models.CharField(max_length=70)
    registration_required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'django_flatpage'


class DjangoFlatpageSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    flatpage = models.ForeignKey(DjangoFlatpage, models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_flatpage_sites'
        unique_together = (('flatpage', 'site'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class QuestionsBoard(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=1)

    class Meta:
        managed = False
        db_table = 'questions_board'


class QuestionsChapter(models.Model):
    id = models.BigAutoField(primary_key=True)
    chapter_id = models.SmallIntegerField(blank=True, null=True)
    chapter = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField()
    board = models.ForeignKey(QuestionsBoard, models.DO_NOTHING, blank=True, null=True)
    class_name = models.ForeignKey('QuestionsClass', models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey('QuestionsSubject', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions_chapter'
        unique_together = (('chapter', 'chapter_id'),)


class QuestionsClass(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.SmallIntegerField()
    status = models.BooleanField()
    icon = models.CharField(max_length=100)
    board = models.ForeignKey(QuestionsBoard, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions_class'
        unique_together = (('board', 'name'),)


class QuestionsQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    marks = models.SmallIntegerField()
    question = models.CharField(max_length=600, blank=True, null=True)
    option1 = models.CharField(max_length=200, blank=True, null=True)
    option2 = models.CharField(max_length=200, blank=True, null=True)
    option3 = models.CharField(max_length=200, blank=True, null=True)
    option4 = models.CharField(max_length=200, blank=True, null=True)
    answer = models.SmallIntegerField(blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    status = models.BooleanField()
    chapter = models.ForeignKey(QuestionsChapter, models.DO_NOTHING, blank=True, null=True)
    board = models.ForeignKey(QuestionsBoard, models.DO_NOTHING, blank=True, null=True)
    class_name = models.ForeignKey(QuestionsClass, models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey('QuestionsSubject', models.DO_NOTHING, blank=True, null=True)
    topic = models.ForeignKey('QuestionsTopic', models.DO_NOTHING, blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions_question'


class QuestionsSubject(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=100)
    total_type_questions = models.SmallIntegerField(blank=True, null=True)
    status = models.BooleanField()
    icon = models.CharField(max_length=100)
    board = models.ForeignKey(QuestionsBoard, models.DO_NOTHING, blank=True, null=True)
    class_name = models.ForeignKey(QuestionsClass, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions_subject'
        unique_together = (('name', 'class_name'),)


class QuestionsTopic(models.Model):
    id = models.BigAutoField(primary_key=True)
    topic_id = models.SmallIntegerField(blank=True, null=True)
    topic = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    chapter = models.ForeignKey(QuestionsChapter, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions_topic'
