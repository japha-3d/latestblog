from django.db.models import query
from django.shortcuts import render,HttpResponse,redirect
from .models import Post,Contact
from django.urls import  reverse_lazy
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import DetailView,CreateView

def AllPost(request):
    all=Post.objects.all()
    return render(request,'home.html',{'allposts':all})
def PostAll(request):
    all_list=Post.objects.all()
    page=request.GET.get('page', 1)
    paginator=Paginator(all_list,21)
    try:
        all = paginator.page(page)
    except PageNotAnInteger:
        all = paginator.page(1)
    except EmptyPage:
        all = paginator.page(paginator.num_pages)
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
def Meet(request):
    if request.method=='POST':
        name = request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        ins=Contact(name=name,email=email,message=message)
        ins.save()
        return redirect("/")
    return render(request,"contact.html")
def policy(request):
    return render(request,"policy.html")