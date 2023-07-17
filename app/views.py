from django.shortcuts import render
from django.http import HttpResponse

from .models import People


# Create your views here.
def home(request):
    return render(request, 'home.html')


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')

        person = People(name=name, school=school, email=email)
        person.save()

    # print(name, school, email)
    return HttpResponse("Success")
    # return render(request, 'home.html')


def people(request):
    d = People.objects.all()

    return render(request, 'people.html', {
        "data": d
    })
