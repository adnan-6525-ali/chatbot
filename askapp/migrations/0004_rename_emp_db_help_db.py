# Generated by Django 4.1.7 on 2023-07-29 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askapp', '0003_rename_emp_phone_emp_db_phone_num_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emp_db',
            new_name='help_db',
        ),
    ]
