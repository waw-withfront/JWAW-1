# Generated by Django 3.1.6 on 2021-12-02 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendant', '0003_auto_20211202_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_parent',
            new_name='student_classroom',
        ),
    ]
