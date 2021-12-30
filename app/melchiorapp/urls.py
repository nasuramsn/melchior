from django.urls import path

from .views.manager import Manager

urlpatterns = [
    path('api/manager/checkcsrf/', Manager.check_csrf, name='managerCheckCsrf'),
    path('api/manager/login/', Manager.login, name='managerLogin'),
]
