# Generated by Django 4.2.6 on 2023-10-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClosedEndedQuestionPossibleAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.CharField(max_length=25)),
                ('B', models.CharField(max_length=25)),
                ('C', models.CharField(max_length=25)),
                ('D', models.CharField(max_length=25)),
                ('E', models.CharField(max_length=25, null=True)),
            ],
        ),
    ]
