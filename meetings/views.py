from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Meeting
from .models import Room


# a function to show the meeting details.
def details(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/details.html", {"meeting": meeting})


# a function to show the meeting details.
def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, "rooms/templates/meetings/rooms.html", {"rooms": rooms})


MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == "POST":
        # The user just submitted the form
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})