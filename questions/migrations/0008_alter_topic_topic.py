# Generated by Django 4.0.4 on 2022-05-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_alter_topic_options_alter_topic_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]