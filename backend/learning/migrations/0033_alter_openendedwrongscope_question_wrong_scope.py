# Generated by Django 4.2.6 on 2024-01-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0032_alter_openendedquestion_category_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openendedwrongscope',
            name='question_wrong_scope',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]