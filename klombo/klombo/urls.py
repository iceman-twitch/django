# urls.py
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('backend/', admin.site.urls),
    path('', include('frontend.urls')),
]#  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)