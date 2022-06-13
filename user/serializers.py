from rest_framework import serializers

from user.models import ShowroomUser


class ShowroomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomUser
        fields = [
            "username",
            "email",
            "password",
            "is_customer",
            "is_dealer",
            "is_showroom",
        ]

    def create(self, validated_data):
        user = ShowroomUser(
            email=validated_data["email"], username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
