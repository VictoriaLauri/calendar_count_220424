from django.shortcuts import render
import datetime

today = datetime.datetime.now()
def get_halloween(date):
    next_halloween = datetime.datetime(date.year, 10, 31)
    if date > next_halloween:
        next_halloween = datetime.datetime(date.year + 1, 10, 31)
    return (next_halloween - date)

days = get_halloween(today).days

# Create your views here.
def index(request):
    return render(request, "halloween/index.html", {
        "days": days,
    })