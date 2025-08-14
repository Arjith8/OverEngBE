"""URLs for user profile management."""

from django.urls import path

from users.views import UserProfileView

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="update_profile_pic"),
]
