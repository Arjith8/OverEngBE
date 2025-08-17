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
    profile_picture = ImageField(required=True, allow_empty_file=False)


class UpdateUserProfileRequestType(TypedDict):
    profile_picture: str


logger = logging.getLogger(__name__)


class UserProfileView(APIView):
    """
    View to handle user profile related actions.
    """

    def get(self, _: Request) -> Response:
        """
        Handle GET requests to retrieve user profile.
        """
        user = User.objects.filter(id=1).first()
        if not user:
            logger.error("User with ID 1 does not exist.")
            return Response({"error": "User does not exist."}, status=404)

        profile = UserProfile.objects.filter(user=user).first()
        if not profile:
            logger.info("No profile found for user ID %s", user.pk)
            return Response({"message": "No profile found."}, status=404)

        data = {"profile_picture": profile.profile_pic.url if profile.profile_pic else None}

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        """
        Handle POST requests to update user profile.
        """
        data = request.data
        serializer = UpdateUserProfileSerializer(data=data)
        if not serializer.is_valid():
            logger.error("Invalid data provided for user profile update. Errors: %s", serializer.errors)
            return Response({"error": "Invalid data provided."}, status=status.HTTP_400_BAD_REQUEST)

        data = cast("UpdateUserProfileRequestType", serializer.validated_data)

        user = User.objects.filter(id=1).first()
        if not user:
            logger.error("User with ID 1 does not exist.")
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)

        profile = UserProfile.objects.filter(user=user).first()
        if not profile:
            logger.info("Creating new user profile for user ID %s", user.pk)
            profile = UserProfile(user=user)

        profile.profile_pic = data.get("profile_picture", profile.profile_pic)  # type: ignore[reportAttributeAccessIssue]
        profile.save()

        return Response({"message": "User profile updated successfully."}, status=status.HTTP_200_OK)
