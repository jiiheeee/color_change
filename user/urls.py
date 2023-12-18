from django.urls import path
from .views import UserDetailView

urlpatterns = [
    path("UserDetail/", UserDetailView.as_view())
]
