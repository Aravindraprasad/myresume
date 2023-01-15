from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination , Review
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):
    dests = Destination.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        print(name,email,desc)
        obj = Review()
        obj.name = name
        obj.email = email
        obj.desc = desc
        obj.save()

        return render(request,'index.html', {'dests':dests})
    else:        
        dests = Destination.objects.all()
        return render(request,'index.html', {'dests':dests})

                                           