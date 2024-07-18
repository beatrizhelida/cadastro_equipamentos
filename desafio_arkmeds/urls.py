from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_desafio.urls')), 
    path('', RedirectView.as_view(url='/api/equipamentos/', permanent=False)),  
]