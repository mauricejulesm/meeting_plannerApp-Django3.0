from django.shortcuts import render

# Create your views here.
from .models import Meeting


def details(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/details.html", {"meeting": meeting})
