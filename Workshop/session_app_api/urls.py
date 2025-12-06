from rest_framework.routers import DefaultRouter
from Workshop.ConferenceApp import admin
from Workshop.session_app_api.views import SessionViewSet
from django.urls import path, include



router = DefaultRouter()
router.register(r'sessions', SessionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path ('conference/', include("ConferenceApp.urls")),
    path ('users/', include("UserApp.urls")),
    path ('sessions/', include("SessionApp.urls")),
]
