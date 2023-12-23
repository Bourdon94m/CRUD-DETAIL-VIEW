from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from Blog.models import BlogPost
# Create your views here.


class BlogPostIndexView(ListView):
    model = BlogPost
    template_name = 'members/index.html'
    context_object_name = 'posts'


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'members/creates.html'
    fields = '__all__'
    success_url = reverse_lazy('index')
    

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'members/detail.html'
    context_object_name = 'detail'






