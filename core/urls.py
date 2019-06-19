from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_jwt.views import obtain_jwt_token



urlpatterns = [
    path('signup/', views.user_create.as_view(), name='signup'),
    path('login/', obtain_jwt_token)
]
