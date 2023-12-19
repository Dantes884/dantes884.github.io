from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import swagger

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.movie.urls')),
    path('movies/', include('apps.movie_web.urls')),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

urlpatterns += swagger.urlpatterns
