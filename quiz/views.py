from django.shortcuts import render, redirect, get_object_or_404
from .models import QuizQuestionsAbcd
from django.core.paginator import Paginator
import random

def home(request):
    return render(request, "home.html")

# def quiz_questions(request):
#     if request.method == "GET":
#         return render(request, "quiz_questions.html")
#     else:
#         n_rows = QuizQuestionsAbcd.objects.count()
#         rand_num = random.randint(1,n_rows+1)
#         question = get_object_or_404(QuizQuestionsAbcd, pk=rand_num)
#         return render(request, "quiz_questions.html",{"num":rand_num,"question":question})

def quiz_questions(request):

    if request.method == "GET":
        return render(request, "quiz_questions.html")

    else:

        quest_base = QuizQuestionsAbcd.objects.all()

        if request.POST.get("type") == "oddz_sys":
            selected_base = quest_base.filter(type = "oddz_sys")
        elif request.POST.get("type") == "pietr_oddz":
            selected_base = quest_base.filter(type = "pietr_oddz")
        elif request.POST.get("type") == "pietr_sys":
            selected_base = quest_base.filter(type = "pietr_sys")
        elif request.POST.get("type") == "sys_era":
            selected_base = quest_base.filter(type = "sys_era")
        
        n_rows = selected_base.count()
        selected_base_ids = list(selected_base.values_list("id",flat=True))
        randomlist = random.sample(selected_base_ids, n_rows)
        question = get_object_or_404(selected_base, pk=randomlist[0])

        return render(request, "quiz_questions.html",{"n_rows":n_rows,"list":randomlist,"question":question})

