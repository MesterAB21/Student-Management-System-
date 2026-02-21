from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("school.urls")),
    path('student/',include("student.urls")),
    path('auth/',include("AuthHome.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
