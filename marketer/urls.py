import os
from django.contrib import admin

from django.urls import path

# from .views import ConfirmAccount

app_name = os.path.dirname(__file__)
print(app_name)

urlpatterns = [
        path('admin/', admin.site.urls),
    ]