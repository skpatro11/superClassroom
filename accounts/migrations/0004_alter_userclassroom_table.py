# Generated by Django 3.2.7 on 2021-09-16 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_classroomuser_userclassroom'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userclassroom',
            table='user_classrooms',
        ),
    ]
