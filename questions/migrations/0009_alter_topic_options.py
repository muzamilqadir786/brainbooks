# Generated by Django 4.0.4 on 2022-06-08 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_alter_topic_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['subject_id', 'topic']},
        ),
    ]
