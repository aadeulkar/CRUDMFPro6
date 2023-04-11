# Generated by Django 4.0.5 on 2022-06-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('fname', models.CharField(max_length=80)),
                ('dob', models.DateField()),
                ('mail', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=25)),
            ],
        ),
    ]