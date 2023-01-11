from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import wiews

app_name = "main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", wiews.AboutMe, name="home"),
    path("projects/", include('projects.urls')),
    path("account/",include("acounts.urls")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
