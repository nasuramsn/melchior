from django.contrib import admin
import logging
# import os

from .models.Company import Company, CompanyLog


logger = logging.getLogger('django')
# logger.info(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Register your models here.

admin.site.register(Company)
admin.site.register(CompanyLog)
