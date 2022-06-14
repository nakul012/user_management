from user_management.models import User,UserProfile,Hobbies,Address
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        email = data["email"]
        password = data["password"]

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    raise ValidationError("User is deactivated")
            else:
                raise ValidationError("Unable to login with given credentials")
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):

        user = User.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            password=make_password(validated_data["password"])
        )
        profile=UserProfile.objects.create(user=user)
        profile.save()
        return user
    


class AddressSerializer(serializers.ModelSerializer):

    class Meta:

        model = Address
        fields = '__all__'

class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:

        model = Hobbies
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    address=AddressSerializer(many=True,read_only=True)
    hobbies=HobbiesSerializer(many=True,read_only=True)

    class Meta:

        model = UserProfile
        fields = ["id","user","phone_number","profile_pic",
        "gender","address","hobbies"]





