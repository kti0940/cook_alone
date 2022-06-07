from django.shortcuts import render, redirect
from .models import Recipe, Timecate, Diffcate
from .forms import *
from django.http import HttpResponse
from webScrapping.models import DefaultRecipe

# Create your views here.

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/list')
    else:
        return redirect('/signin')

def view_list(request):
    if request.method == 'GET':
        recipe = Recipe.objects.all()
        all_recipe = DefaultRecipe.objects.all()

        return render(request, 'list.html', {'recipes': all_recipe})

def upload_recipes(request):
    if request.method == 'GET':
        ur_user = request.user.is_authenticated
        if ur_user:
            timecate = Timecate.objects.all()
            diffcate = Diffcate.objects.all()
            return render(request, 'upload.html', {'timecost': timecate, 'difficulty': diffcate})
        else:
            return redirect('/')

    elif request.method == 'POST':
        author = request.user
        title = request.POST.get('title','')
        img_url = request.FILES.get('image_url','')
        timecost = request.POST.get('timecost','')
        difficulty = request.POST.get('difficulty','')
        ingredient = request.POST.get('ingredient','')
        cookstep = request.POST.get('ingredient','')
        print(author)
        print(img_url)
        print(title)
        print(timecost)
        print(difficulty)
        print(ingredient)
        print(cookstep)

        Recipe(
            author=author,
            title=title,
            img_url=img_url,
            timecost=timecost,
            difficulty=difficulty,
            ingredient=ingredient,
            cookstep=cookstep,

        ).save()

        return HttpResponse('success')




