from django.db.models import query
from django.shortcuts import render,HttpResponse
from .models import Post

from django.views.generic import DetailView

def AllPost(request):
    all=Post.objects.all()
    return render(request,'home.html',{'allposts':all})
def PostAll(request):
    all=Post.objects.all()
    return render(request,'all.html',{'allposts':all})
def Trending(request):
    all=Post.objects.all()
    return render(request,'trending.html',{'allposts':all})
# Create your views here.
class Detail(DetailView):
    model=Post
    template_name="detail.html"
def Search(request):
    query=request.GET['query']
    allposts=Post.objects.filter(title__icontains=query)
    return render(request,"search.html",{'allposts':allposts})
    #return HttpResponse("Good")