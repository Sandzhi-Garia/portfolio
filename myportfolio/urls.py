from django.contrib import admin
from django.urls import path
from portfolio.views import home, about, projects, workExperience, education, contact_view
from django.shortcuts import render  # для contact_success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('workExperience/', workExperience, name='workExperience'),
    path('contact/', contact_view, name='contact'),
    path('education/', education, name='education'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
