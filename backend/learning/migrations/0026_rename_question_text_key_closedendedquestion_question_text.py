# Generated by Django 4.2.6 on 2023-12-17 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0025_rename_question_category_closedendedquestion_category_key_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='closedendedquestion',
            old_name='question_text_key',
            new_name='question_text',
        ),
    ]
