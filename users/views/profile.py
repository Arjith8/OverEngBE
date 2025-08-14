"""View to handle CRUD operations for user profile."""

import logging
from typing import TypedDict, cast

from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ImageField, Serializer
from rest_framework.views import APIView, status

from users.models import UserProfile


class UpdateUserProfileSerializer(Serializer):
    profile_picture = ImageField(required=False)


class UpdateUserProfileRequestType(TypedDict):
    profile_picture: str | None


logger = logging.getLogger(__name__)


class UserProfileView(APIView):
    """
    View to handle user profile related actions.
    """

    def post(self, request: Request) -> Response:
        """
        Handle POST requests to update user profile.
        """
        data = request.data
        serializer = UpdateUserProfileSerializer(data=data)
        if not serializer.is_valid():
            logger.error("Invalid data provided for user profile update. Errors: %s", serializer.errors)
            return Response({"error": "Invalid data provided."}, status=400)

        data = cast("UpdateUserProfileRequestType", serializer.validated_data)
        user = User.objects.filter(id=1).first()
        if not user:
            logger.error("User with ID 1 does not exist.")
            return Response({"error": "User does not exist."}, status=404)

        profile = UserProfile.objects.filter(user=user).first()
        if not profile:
            logger.info("Creating new user profile for user ID %s", user.pk)
            profile = UserProfile(user=user)

        profile.profile_pic = data.get("profile_picture", profile.profile_pic)
        profile.save()

        return Response({"message": "User profile updated successfully."}, status=status.HTTP_200_OK)
