from django.contrib import admin
from django.urls import path
# from AppPE import views
from AppPE.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
]
