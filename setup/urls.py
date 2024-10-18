from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin está no projeto principal
    path('', include('comunicacao.urls')),  # Inclui URLs do app comunicacao
]
