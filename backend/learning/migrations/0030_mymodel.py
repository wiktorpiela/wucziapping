# Generated by Django 4.2.6 on 2023-12-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0029_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field', models.CharField(max_length=20)),
            ],
        ),
    ]
