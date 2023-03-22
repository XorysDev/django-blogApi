from django.urls import path, include
from post import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),

]