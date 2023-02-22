"""dvizhenie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app_events.views import *
from app_news.views import *
from app_root.views import *
from app_questions.views import *
from app_projects.views import *

from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import debug_toolbar

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Апишка <3",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()

router.register(r'events', EventViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'gallery', GalleryViewSet)

router.register(r'news', NewsViewSet)

router.register(r'projects', ProjectViewSet)
router.register(r'partners', PartnerViewSet)

router.register(r'files', FileViewSet)
router.register(r'contacts', ContactsViewSet)

router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
