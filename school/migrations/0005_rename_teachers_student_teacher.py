# Generated by Django 3.2.6 on 2021-08-09 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_student_teachers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teachers',
            new_name='teacher',
        ),
    ]
