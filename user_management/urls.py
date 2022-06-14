from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user_management.views import LoginView,SignUpView,UserProfileListView,UserListView,AddressListView,HobbiesListView

urlpatterns = [
    path('register', SignUpView.as_view() ),
    path('user', UserListView.as_view() ),
    path('login', LoginView.as_view() ),
    path('profile', UserProfileListView.as_view() ),
    path('profile/<int:pk>', UserProfileListView.as_view() ),
    path('address', AddressListView.as_view() ),
    path('address/<int:pk>', AddressListView.as_view() ),
    path('hobbies', HobbiesListView.as_view() ),
    path('hobbies/<int:pk>', HobbiesListView.as_view() ),
    
]



if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)