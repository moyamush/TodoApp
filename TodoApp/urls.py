"""TodoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django_registration.backends.one_step.views import RegistrationView


from todo.forms import CustomUserForm
# from core.views import IndexTemplateView

import todo.views as todo

import rest_framework.authtoken.views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('mail/', todo.display_mail),
    path('accounts/register/', RegistrationView.as_view(form_class=CustomUserForm, success_url="/"),
                                                        name="django-registration_register"),
    path('accounts/', include("django_registration.backends.one_step.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    # # api画面でユーザーの切り替えができるようになる
    path('api-auth/', include("rest_framework.urls")),
    path('api/rest-auth/', include("rest_auth.urls")),
    path('api/rest-auth/registration/', include("rest_auth.registration.urls")),
    path("api/", include("todo.api.urls")),
    # re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
    #追加
    #api/authアプリケーションのURLconf読み込み
    # path('api/jwt/auth/', include('djoser.urls.jwt')),
     path('api-token-auth/', auth_views.obtain_auth_token)
]
