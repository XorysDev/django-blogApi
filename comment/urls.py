from django.urls import path
from comment import views

urlpatterns = [
    path('', views.CommentCreateView.as_view()),
    path('<int:pk>/', views.CommentDetailView.as_view()),
]