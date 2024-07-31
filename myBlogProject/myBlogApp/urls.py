from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>/", views.post_details, name="post"),
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.user_logout, name="logout"),
    path("newstory/", views.newstory, name="newstory"),
    path("post/<int:pk>/comment/", views.comment, name="comment"),
]
