from django.urls import path
from ratings import views

urlpatterns = [
    path('ratings/', views.RatingList.as_view()),
    path('ratings/<int:pk>/', views.RatingDetailView.as_view()),
    path('articles/<int:article_id>/rating-stats/',
         views.article_rating_stats, name='article-rating-stats'),
]
