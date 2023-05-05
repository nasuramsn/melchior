from django.urls import path

from .views.manager import Manager
from .views import (dashboard)

urlpatterns = [
    path('api/manager/checkcsrf/', Manager.check_csrf, name='managerCheckCsrf'),
    path('api/manager/login/', Manager.login, name='managerLogin'),
    path('dashboard', dashboard.Dashboard.as_view(), name='dashboard'),
]
