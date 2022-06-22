from django.urls import path
from news.views import *

urlpatterns = [
    path('', NewsListView.as_view()),
    path('news/<int:id>', NewsDetailView.as_view()),
    path('news/category/<int:id>', NewsCategoryView.as_view()),
    path('profile/<int:id>', ProfileView.as_view()),
    path('news/edit/<int:pk>', NewsEditUpdateView.as_view()),
    path('news/create', NewsCreateView.as_view())
]