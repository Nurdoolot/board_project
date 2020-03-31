from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class IndexPageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = "posts"

