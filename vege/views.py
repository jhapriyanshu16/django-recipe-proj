from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def receipes(request):
    if request.method == "POST":
        data  = request.POST

        receipe_description = data.get('receipe_description')
        receipe_name = data.get('receipe_name')
        receipe_image = request.FILES.get('receipe_image')
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        Receipe.objects.create(
            receipe_description = receipe_description,
            receipe_name = receipe_name,
            receipe_image = receipe_image ,
        )

        return redirect('/')
    
    queryset = Receipe.objects.all()
    context = {'receipes':queryset}

    return render(request,"receipes/receipes.html",context)