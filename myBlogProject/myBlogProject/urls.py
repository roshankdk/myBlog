from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =  [
    path('',include('myBlogApp.urls')),
    path('admin/',admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

