"""Internship URL Configuration

The `urlpatterns` list routes URLs to test_views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function test_views
    1. Add an import:  from my_app import test_views
    2. Add a URL to urlpatterns:  path('', test_views.home, name='home')
Class-based test_views
    1. Add an import:  from other_app.test_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.test_urls_ads import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.test_urls_ads'))
"""
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('Internship.internship_app.urls')),
                  path('auth/', include('Internship.internship_auth.urls')),
                  path('profile/', include('Internship.internship_profiles.urls')),
                  path('__debug__/', include(debug_toolbar.urls)),
                  path('summernote/', include('django_summernote.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
