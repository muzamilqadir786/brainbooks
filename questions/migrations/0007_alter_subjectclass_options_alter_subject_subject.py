# Generated by Django 4.0.4 on 2022-05-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_remove_subject_classes_subjectclass'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subjectclass',
            options={'verbose_name_plural': 'Class Subjects'},
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(blank=True, choices=[('URD', 'Urdu'), ('ENG', 'English'), ('ISL', 'Islamiyat'), ('PHY', 'Physics'), ('CHE', 'Chemistry'), ('BIO', 'Biology'), ('MTM', 'Mathematics'), ('CMP', 'Computer'), ('STA', 'Statistics')], default='MIS', max_length=3, unique=True),
        ),
    ]
