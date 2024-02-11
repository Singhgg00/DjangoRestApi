from django.urls import path, include
from rest_api_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path ('hello-view', views.HelloApiView.as_view()),
    path('', include(router.urls))
]