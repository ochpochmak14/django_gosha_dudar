from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name="news"),
    path('create/', views.create, name="create"),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
]
