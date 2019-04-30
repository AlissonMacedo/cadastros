from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# Gabiarra para funcionar os arquivos staticos --------------

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('apps.core.urls')),
    url(r'^', include('apps.dashboard.urls')),
    #path('tecnologiadainformacao/', include('apps.tecnologiadainformacao.urls')), Exemplo
    path('login/', auth_views.LoginView.as_view(), name='login'), # Importa view de login do Django

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

