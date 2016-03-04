from django.http import HttpResponse


from django.shortcuts import render
from .models import School


def read(request):
    namea=request.POST['name']
    rolla=request.POST['roll']
    ab = School(name=namea,roll=rolla)
    ab.save()

    return HttpResponse('<p>"Your details has been saved"</p></br><a href="..">"Go to home"</a>')



def index(request):
    ab = School.objects.all()
    context = {'ab': ab}
    return render(request, 'student/index.html', context)

def search(request):
    ab = School.objects.all()
    namea=request.POST['name']
    rolla=request.POST['roll']
    context = {'ab': ab,'namea':namea,'rolla':rolla}
    return render(request, 'student/search.html', context)