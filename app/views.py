

from django.shortcuts import render, redirect
from .models import Student

def index(request):
    data = Student.objects.all()
    print(data)
    context = {"data": data}
    return render(request, "index.html", context)

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(name, email, age, gender)
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")

def updateData(request, id):
    d = Student.objects.get(id=id)
    if request.method == "POST":
        d.name = request.POST['name']
        d.email = request.POST['email']
        d.age = request.POST['age']
        d.gender = request.POST['gender']
        print(d.name, d.email, d.age, d.gender)
        d.save()
        return redirect("/")
    context = {"d": d}
    return render(request, "edit.html", context)

def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")



