from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Applications principales
    path('Conference/', include("ConferenceApp.urls")),
    path('users/', include("UserApp.urls")),
    path("api/", include("session_app_api.urls")),
    path("security/", include("securityConfigApp.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
