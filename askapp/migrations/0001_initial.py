# Generated by Django 4.1.7 on 2023-07-29 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Message', models.CharField(max_length=255)),
                ('date_time', models.DateField(null=True)),
            ],
        ),
    ]