from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html", {"meetings_count": Meeting.objects.count()})


def about(request):
    return HttpResponse("My name is Maurice Jules Mulisa, I will be the best python programmer in Rwanda!")
