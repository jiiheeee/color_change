from django.urls import path
from .views import UserDetailView, LogInView

urlpatterns = [
    path("<int:user_id>", UserDetailView.as_view()),
    path("login/", LogInView.as_view())
]
