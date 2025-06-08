from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Nemoone.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]

# Serve static files in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

