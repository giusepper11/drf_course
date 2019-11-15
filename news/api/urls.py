from django.urls import path

from news.api.views import ArticleListCreateAPIView, JournalistListCreate, ArticleDetailAPIView

urlpatterns = [
    # path('articles/', article_list_create_api_view, name='article-list'),
    # path('articles/<int:pk>', article_detail_api_view, name='article-list')

    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>', ArticleDetailAPIView.as_view(), name='article-detail'),

    path('journalists/', JournalistListCreate.as_view(), name='journalist-list'),
]
