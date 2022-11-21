from lib2to3.pygram import pattern_grammar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls') ),
    path('', include('plataforma.urls'))
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
