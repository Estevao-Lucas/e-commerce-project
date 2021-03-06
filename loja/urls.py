from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('produto.urls')),
    path('perfil/', include('perfil.urls')),
    path('pedido/', include('pedido.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls'))
                  #TODO Remover após finalização do projeto debug toolbar
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
