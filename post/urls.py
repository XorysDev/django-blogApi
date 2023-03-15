from django.urls import path
from post import views

urlpatterns = [
    path('', views.PostListCreateView.as_view()),
    path('<int:pk>/', views.PostDetailView.as_view()),
]