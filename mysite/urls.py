from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('guidance_emu.urls')),
    path('otakara', include('otakara.urls')),
    #path('admin/', admin.site.urls),
]