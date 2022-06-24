from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, FormView, UpdateView, CreateView
from news.services.news_service import *
from news.services.user_service import *


class NewsListView(ListView):
    template_name = 'news_list.html'
    queryset = get_all_news()
    context_object_name = 'all_news'


class NewsDetailView(View):
    template_name = 'news_detail.html'

    def get(self, request, id):
        news = get_news_by_id(id)
        return render(request, self.template_name, {'news': news})


class ProfileView(View):
    template_name = 'profile.html'

    def get(self, request, id):
        user = get_user_by_id(id)
        return render(request, self.template_name, {'user': user})


class NewsCategoryView(View):
    template_name = 'news_list.html'

    def get(self, request, id):
        news = get_news_by_category(id)
        return render(request, self.template_name, {'all_news': news})


class NewsEditUpdateView(UpdateView):
    model = News
    fields = ['title', 'summary', 'body']
    template_name = 'news_edit_form.html'
    # template_name_suffix = "_edit_form"
    success_url = '/profile/10'
    context_object_name = 'news'


class NewsCreateView(CreateView):
    model = News
    fields = ['title', 'summary', 'body', 'category', 'user']
    template_name = 'news_create_form.html'
    # template_name_suffix = "_create_form"
    success_url = '/profile/10'
