"""dot_test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

from myapi.views import CarView

urlpatterns = [
    # Needed for locale change
    # path('i18n/', include('django.conf.urls.i18n')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path("cars/", CarView.as_view())
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),    
)
