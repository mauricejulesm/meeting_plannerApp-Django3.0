from datetime import datetime

from django.http import HttpResponse


# Create your views here.


def welcome(request):
    return HttpResponse("Welcome to the meeting planner app!")


def about(request):
    return HttpResponse("My name is Maurice Jules Mulisa, I will be the best python programmer in Rwanda!")
