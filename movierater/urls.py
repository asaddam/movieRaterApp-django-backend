from django.contrib import admin
from django.urls import path
from django.conf.urls import include # 2 new line
from rest_framework.authtoken.views import obtain_auth_token #11

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # 3 new line
    path('auth/', obtain_auth_token), # 11
]
