from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator 
from .models import Blog
from django.db.models import Q

# Create your views here.
def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request,'home.html',{'blogs':blogs,'posts':posts})

def new(request):
    return render(request, 'new.html')

def detail(request, blog_id):
    details= get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details': details})
   
def create(request):
        print(request)
        blog= Blog()
        blog.title = request.POST.get('title','')
        blog.body = request.POST.get('body','')
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/' + str(blog.id))    

def mypage(request):
    return render(request, 'mypage.html')

def mypage2(request):
    return render(request, 'mypage2.html')

def nono(request):
    return render(request, 'nono.html')

def index(request):
    return render(request, 'index.html')  

def search(request):
        schWord= '%s' % request.POST['search_word']
        post_list= Blog.objects.filter(Q(title__icontains=schWord) |
                Q(body__icontains=schWord)).distinct()

        context={}
        context['search_term']=schWord
        context['object_list']=post_list

        return render(request, 'post_search.html', context)