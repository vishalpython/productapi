from django.urls import path,include

from .views import CreateUserView,UserLoginView,ManageUserView

urlpatterns = [
    path('create/', CreateUserView.as_view(),name='create'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('me/',ManageUserView.as_view(),name='me'),
]