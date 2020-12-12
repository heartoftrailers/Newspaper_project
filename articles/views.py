from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):  #LoginRequiredMixin  and login_url = 'login'  are used to limit the non-user( they are can only view,del,update if login)
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'
class ArticleDetailView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'
class ArticleDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView): # UserPassesTestMixin and def test_func(self): doesn't allow any other user to delete posts from different user
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):# UserPassesTestMixin and def test_func(self): doesn't allow any other user to delete posts from different user
    model = Article
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)