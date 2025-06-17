from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
urlpatterns = [
#    path('admin/', admin.site.urls) ,
#    path('', include('frontend.urls') ),
]
urlpatterns += i18n_patterns( 
        path('admin/', admin.site.urls) ,
        path('', include('frontend.urls') ),
    )
