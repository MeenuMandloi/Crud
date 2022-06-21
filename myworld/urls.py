from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('member/', include('member.urls')),
    path('admin/', admin.site.urls),
]
