from django.shortcuts import render,redirect
import requests
from django.views.generic import TemplateView
import math
from movie_app.models import Movie_Review
from movie_app.forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,DetailView
from  django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    
@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'myprofile.html'

@login_required
def review(request,pk):
    ls={}
    url='http://www.omdbapi.com/?i=%s&apikey=67533bbf' %pk
    response = requests.get(url)
    ls = response.json()
    mylist = Movie_Review.objects.filter(User=request.user,title=ls['Title']).order_by('-reviewrating')

    if mylist:
        return render(request,'already.html')
    else:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.User = request.user
                review.title = ls['Title']
                review.year = ls['Year']
                review.poster = ls['Poster']
                review.movietype = ls['Type']
                review.imdb = ls['imdbID']
                review.save()
                return redirect('dash')
        else:
            form = ReviewForm()
        return render(request,'movie_review_form.html',{'form':form})

@method_decorator(login_required, name='dispatch')
class OwnList(ListView):
    model = Movie_Review
    template_name = 'ownreview.html'

    def get_queryset(self):
        return Movie_Review.objects.filter(User=self.request.user).order_by('-reviewrating')




def movie_default(request):
    movie_list={}
    query=str('one')
    url = 'http://www.omdbapi.com/?s=%s&apikey=67533bbf' % query
    response = requests.get(url)
    movie_list = response.json()
    total=int(movie_list['totalResults'])
    page=math.ceil(total/10)
    current_page=1
    nex=int(current_page + 1)
    if (page==1) or (page==2):
        return render(request, 'only-one.html', {'movie_list': movie_list,'curr':current_page})
    else:
        return render(request, 'movie-search.html', {'movie_list': movie_list,'page':page,'curr':current_page,'next':nex,'quer':query})



def movie_search(request):
    movie_list={}
    if 'query' in request.GET:
        query = request.GET['query']
        url = 'http://www.omdbapi.com/?s=%s&apikey=67533bbf' % query
        response = requests.get(url)
        movie_list = response.json()
        total=int(movie_list['totalResults'])
        page=math.ceil(total/10)
        current_page=1
        nex=int(current_page + 1)
        if (page==1) or (page==2):
            return render(request, 'only-one.html', {'movie_list': movie_list,'curr':current_page})
        else:
            return render(request, 'movie-search.html', {'movie_list': movie_list,'page':page,'curr':current_page,'next':nex,'quer':query})


def movie_detail(request,pk):
    movie_detail={}
    url='http://www.omdbapi.com/?i=%s&apikey=67533bbf' %pk
    response = requests.get(url)
    movie_detail = response.json()
    return render(request, 'movie-detail.html',{'movie_detail':movie_detail})

def movie_review_detail(request,pk):
    movie_detail={}
    url='http://www.omdbapi.com/?i=%s&apikey=67533bbf' %pk
    response = requests.get(url)
    movie_detail = response.json()
    return render(request, 'review_page.html',{'movie_detail':movie_detail})


def movie_next_page(request,quer,nex):
    movie_list={}
    query=quer
    url = 'http://www.omdbapi.com/?s=%s&page=%s&apikey=67533bbf' % (query,nex)
    response = requests.get(url)
    movie_list = response.json()
    total=int(movie_list['totalResults'])
    page=math.ceil(total/10)
    current_page=nex
    nex=int(current_page + 1)
    prev=int(current_page-1)
    if current_page==page:
        return render(request, 'movie_last.html', {'movie_list': movie_list,'page':page,'curr':current_page,'quer':query,'prev':prev})
    else:
        return render(request, 'movie_next.html', {'movie_list': movie_list,'page':page,'curr':current_page,'next':nex,'quer':query,'prev':prev})

def movie_prev_page(request,quer,prev):
    movie_list={}
    query=quer
    url = 'http://www.omdbapi.com/?s=%s&page=%s&apikey=67533bbf' % (query,prev)
    response = requests.get(url)
    movie_list = response.json()
    total=int(movie_list['totalResults'])
    page=math.ceil(total/10)
    current_page=prev
    nex=int(current_page + 1)
    prev=int(current_page-1)
    if (prev==0):
        return render(request, 'movie-search.html', {'movie_list': movie_list,'page':page,'curr':current_page,'next':nex,'quer':query})
    else:  
        return render(request, 'movie_next.html', {'movie_list': movie_list,'page':page,'curr':current_page,'next':nex,'quer':query,'prev':prev})


def movie_first_page(request,quer):
    movie_list={}
    query=quer
    url = 'http://www.omdbapi.com/?s=%s&apikey=67533bbf' % (query)
    response = requests.get(url)
    movie_list = response.json()
    total=int(movie_list['totalResults'])
    page=math.ceil(total/10)
    current_page=1
    nex=int(current_page+1)
    return render(request, 'movie-search.html', {'movie_list': movie_list,'page':page,'curr':current_page,'quer':query,'next':nex})

def movie_last_page(request,quer,pag):
    movie_list={}
    query=quer
    url = 'http://www.omdbapi.com/?s=%s&page=%s&apikey=67533bbf' % (query,pag)
    response = requests.get(url)
    movie_list = response.json()
    total=int(movie_list['totalResults'])
    page=math.ceil(total/10)
    current_page=page
    prev=int(current_page-1)
    return render(request, 'movie_last.html', {'movie_list': movie_list,'page':page,'curr':current_page,'quer':query,'prev':prev})

