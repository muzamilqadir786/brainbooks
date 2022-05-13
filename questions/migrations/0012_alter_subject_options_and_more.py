# Generated by Django 4.0.4 on 2022-05-10 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_alter_unit_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='subjectclass',
            old_name='subject',
            new_name='subject_name',
        ),
        migrations.AlterUniqueTogether(
            name='subjectclass',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='subjectclass',
            name='subject_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.class', verbose_name='Class'),
        ),
        migrations.AlterUniqueTogether(
            name='subjectclass',
            unique_together={('subject_class', 'subject_name')},
        ),
    ]
