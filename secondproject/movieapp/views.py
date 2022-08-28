from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import context
from . models import movies
from .forms import Form
# Create your views here.
def index(request):
    Movie=movies.objects.all()
    context={
        'movies':Movie
    }
    return render(request,"index.html",context)
def list(request,movie_id):
    Movie=movies.objects.get(id=movie_id)
    return render(request,"list.html",{'movie':Movie})
def add(request):
    if request.method=='POST':
        Movie_Name = request.POST.get('Movie_Name','')
        Movie_description = request.POST.get('Movie_description','')
        Movie_Year = request.POST.get('Movie_Year','')
        Movie_img = request.FILES['Movie_img']
        Movie = movies(Movie_Name=Movie_Name,Movie_description=Movie_description,Movie_Year=Movie_Year,Movie_img=Movie_img)
        Movie.save()
    return render(request,"add.html")
def update(request,id):
    movie=movies.objects.get(id=id)
    form=Form(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':movie})
def delete(request,id):
    if request.method == 'POST':
        movie = movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')



# Movie = movies(Movie_Name=name,Movie_description=description,Movie_Year=year,Movie_Img=img)