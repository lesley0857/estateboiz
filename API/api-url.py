from django.urls import path
from API.views import *
#from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

app_name = 'API'

urlpatterns = [

    path('list/',list_api.as_view(),name='list_api'),
    path('create/',user_creation_api,name='user_creation_api'),
    path('login/',user_login_api,name='user_login_api'),
    path('list/create_chat/<int:pk>/',chatmessage_create_api.as_view(),name='chatmessage_create_api'),
    path('list/retrieve/<int:id>/',chatmessage_retrieve_api,name='chatmessage_retrieve_api'),
    #path('auth/token/',obtain_jwt_token),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='TokenRefreshView')
    ]