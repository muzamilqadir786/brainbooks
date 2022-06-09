# Generated by Django 4.0.4 on 2022-05-24 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_rename_subject_topic_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.board'),
        ),
        migrations.AddField(
            model_name='topic',
            name='class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.class'),
        ),
        migrations.AddField(
            model_name='topic',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.subject'),
        ),
    ]