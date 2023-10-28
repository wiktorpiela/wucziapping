# Generated by Django 4.2.6 on 2023-10-28 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_delete_closedendedquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosedEndedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_hard', models.BooleanField(default=False)),
                ('correct_answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_ans', to='learning.closedendedquestioncorrectanswer')),
                ('possible_answers_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='possible_ans', to='learning.closedendedquestionpossibleanswers')),
                ('question_text_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_txt', to='learning.closedendedquestiontext')),
            ],
        ),
    ]
