from user_management.models import UserProfile,Hobbies,Address,User
from user_management.serializers import (
    LoginSerializer,
    UserProfileSerializer,
    UserSerializer,AddressSerializer,HobbiesSerializer
)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import mixins, generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import generics






class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        request.user.auth_token.delete()
        django_logout(request)
        return Response({"Message": "successfully logout"}, status=204)


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)



class UserProfileListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    serializer_class = UserProfileSerializer
    parser_classes=(FormParser,MultiPartParser)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()

    def get(self, request, *args, **kwargs):
        params = request.query_params
        if not "pk" in kwargs:
            return self.list(request)
        post = get_object_or_404(UserProfile, pk=kwargs["pk"])
        return Response(UserProfileSerializer(post).data, status=200)
    
    def put(self,request,pk=None):
        return self.update(request,pk)


    def delete(self, request, pk=None):
        return self.destroy(request, pk)

    


class UserListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        params = request.query_params
        print(params)
        if not "pk" in kwargs:
            return self.list(request)
        post = get_object_or_404(User, pk=kwargs["pk"])
        return Response(UserSerializer(post).data, status=200)
    
    def put(self,request,pk=None):
        return self.update(request,pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class AddressListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin):
    serializer_class = AddressSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()

    def get(self, request, *args, **kwargs):
        params = request.query_params
        print(params)
        if not "pk" in kwargs:
            return self.list(request)
        post = get_object_or_404(Address, pk=kwargs["pk"])
        return Response(AddressSerializer(post).data, status=200)
    
    def put(self,request,pk=None):
        return self.update(request,pk)

    def post(self, request):
        data = request.data
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class HobbiesListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    serializer_class = HobbiesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Hobbies.objects.all()

    def get(self, request, *args, **kwargs):
        params = request.query_params
        print(params)
        if not "pk" in kwargs:
            return self.list(request)
        post = get_object_or_404(Hobbies, pk=kwargs["pk"])
        return Response(HobbiesSerializer(post).data, status=200)
    
    def put(self,request,pk=None):
        return self.update(request,pk)

    def post(self, request):
        data = request.data
        serializer = HobbiesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

