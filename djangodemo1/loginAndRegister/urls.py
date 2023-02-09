
from django.contrib import admin
from django.urls import path, re_path
from . import views as v1


# set the namespace
app_name = 'loginAndRegister'
urlpatterns = [
    # Django admin management page
    #path('adminSite/', admin.site.urls),

    # loginAndRegister APP
    path('', v1.index),
    path('index/', v1.index, name='index'),
    path('login/', v1.login, name='login'),
    path('register/', v1.register, name='register'),
    path('logout/', v1.logout, name='logout'),
]
