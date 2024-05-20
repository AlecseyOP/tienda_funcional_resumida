from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


app_name = "Tienda"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('Tienda.urls', namespace='Tienda'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

