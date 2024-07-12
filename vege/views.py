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

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))


    context = {'receipes':queryset}

    return render(request,"receipes/receipes.html",context)


def delete_receipe(request, id ):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')



def update_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    
    if request.method=="POST":
        data  = request.POST
        receipe_description = data.get('receipe_description')
        receipe_name = data.get('receipe_name')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image
        
        queryset.save()

        return redirect('/')
        

    context = {'receipe':queryset}
    return render(request,"receipes/update_receipes.html",context)


