from django.contrib import admin
from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout/", views.log_out, name="logout"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
    path("update-profile/", views.UpdateProfileView.as_view(), name="update"),
    path("verify/", views.LocationVerifyView.as_view(), name="verify"),
    path("verify/complete/", views.verify_complete, name="verify-complete"),
    path("verify/detail/", views.LocationVerifyDetailView.as_view(), name="verify-detail"),
]