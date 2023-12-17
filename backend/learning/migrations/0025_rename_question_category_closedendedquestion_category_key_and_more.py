# Generated by Django 4.2.6 on 2023-12-17 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0024_closedendedquestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='closedendedquestion',
            old_name='question_category',
            new_name='category_key',
        ),
        migrations.RenameField(
            model_name='closedendedquestion',
            old_name='correct_answer',
            new_name='correct_answer_key',
        ),
        migrations.RenameField(
            model_name='closedendedquestion',
            old_name='is_multi',
            new_name='is_multi_key',
        ),
        migrations.RenameField(
            model_name='closedendedquestion',
            old_name='possible_answers',
            new_name='possible_answers_key',
        ),
        migrations.RenameField(
            model_name='closedendedquestion',
            old_name='question_text',
            new_name='question_text_key',
        ),
    ]
