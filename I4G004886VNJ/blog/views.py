from re import template
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import (DeleteView, CreateView, UpdateView)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "blog\post_list.html"

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "blog\post_form.html"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post
    fields = "__all__"
    template_name = "blog\post_detail.html"
    success_url = reverse_lazy("blog:all")

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    template_name = "blog\post_form.html"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")