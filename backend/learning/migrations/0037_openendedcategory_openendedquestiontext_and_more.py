# Generated by Django 4.2.6 on 2024-01-05 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0036_remove_openendedquestion_category_key_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenEndedCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OpenEndedQuestionText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OpenEndedScope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_scope', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='OpenEndedWrongScope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_wrong_scope', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpenEndedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_cat_open', to='learning.openendedcategory')),
                ('quest_txt_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_txt_open', to='learning.openendedquestiontext')),
                ('scope_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_scope_open', to='learning.openendedscope')),
                ('wrong_scope_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_wrong_scope_open', to='learning.openendedwrongscope')),
            ],
        ),
    ]
