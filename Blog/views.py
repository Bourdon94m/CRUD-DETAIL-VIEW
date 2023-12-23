from typing import Any
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Créer"
        return context
    
    
    
    

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'members/detail.html'
    context_object_name = 'detail'


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = '__all__'
    template_name = "members/creates.html"
    success_url = '/'
                
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Modifier"
        return context


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'delete'