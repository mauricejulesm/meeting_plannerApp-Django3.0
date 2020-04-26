from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Meeting


# a function to show the meeting details.
def details(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/details.html", {"meeting": meeting})
