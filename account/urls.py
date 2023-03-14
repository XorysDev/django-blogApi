from dj_rest_auth.views import LoginView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
    path('register/', views.UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', views.CustomLogoutView.as_view()),

]