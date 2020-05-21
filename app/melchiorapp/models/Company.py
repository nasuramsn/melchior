# classes for Company
from django.core.validators import validate_email
from django.db import models

from ..consts.ItemIds import ITEM_ID_COMPANY_ID, ITEM_ID_SERIAL_NUMBER
from ..consts.ItemNames import ITEM_NAME_ADDRESS1, ITEM_NAME_ADDRESS2, ITEM_NAME_COMPANY_ID, \
    ITEM_NAME_DESCRIPTION, ITEM_NAME_EMAIL_ADDRESS1, ITEM_NAME_EMAIL_ADDRESS2, \
    ITEM_NAME_FOUNDED_AT, ITEM_NAME_HOMEPAGE, ITEM_NAME_MARKET_CODE, ITEM_NAME_NAME, \
    ITEM_NAME_POST_CODE, ITEM_NAME_PRESIDENT, ITEM_NAME_SUMMARY, ITEM_NAME_STOCK_CODE, ITEM_NAME_TEL_NO
from ..consts.TableIds import TABLE_ID_COMPANIES, TABLE_ID_COMPANY_LOGS
from .CoreModel import CoreMaster, CoreRecord


class Company(CoreMaster):

    company_id = models.CharField(
        verbose_name=ITEM_NAME_COMPANY_ID, default='', max_length=50)

    def __init__(self, *args, **kwargs):
        self.unique_keys = [ITEM_ID_COMPANY_ID]
        models.Model.__init__(self, *args, **kwargs)

    def get_with_uk(self):
        _self_result = super(Company, self).get_with_uk()
        _company_log = CompanyLog()
        _company_log.company_id = _self_result.company_id
        _company_log.serial_number = _self_result.serial_number
        _log_result = _company_log.get_with_uk()
        _self_result.record = _log_result

        return _self_result

    class Meta:
        db_table = TABLE_ID_COMPANIES


class CompanyLog(CoreRecord):

    company_id = models.CharField(
        verbose_name=ITEM_NAME_COMPANY_ID, default='', max_length=50)
    name = models.CharField(
        verbose_name=ITEM_NAME_NAME, default='', max_length=254)
    post_code = models.CharField(
        verbose_name=ITEM_NAME_POST_CODE, default='', max_length=20)
    address1 = models.CharField(
        verbose_name=ITEM_NAME_ADDRESS1, default='', max_length=254)
    address2 = models.CharField(
        verbose_name=ITEM_NAME_ADDRESS2, default='', max_length=254)
    tel_no = models.CharField(
        verbose_name=ITEM_NAME_TEL_NO, default='', max_length=20)
    email_address1 = models.EmailField(
        verbose_name=ITEM_NAME_EMAIL_ADDRESS1, unique=True, validators=[validate_email])
    email_address2 = models.EmailField(
        verbose_name=ITEM_NAME_EMAIL_ADDRESS2, unique=True, validators=[validate_email])
    homepage_url = models.URLField(verbose_name=ITEM_NAME_HOMEPAGE)
    founded_at = models.CharField(
        verbose_name=ITEM_NAME_FOUNDED_AT, default='', max_length=20)
    president = models.CharField(
        verbose_name=ITEM_NAME_PRESIDENT, default='', max_length=50)
    summary = models.CharField(
        verbose_name=ITEM_NAME_SUMMARY, default='', max_length=200)
    description = models.CharField(
        verbose_name=ITEM_NAME_DESCRIPTION, default='', max_length=4000)
    market_code = models.CharField(
        verbose_name=ITEM_NAME_MARKET_CODE, default='', max_length=50)
    stock_code = models.CharField(
        verbose_name=ITEM_NAME_STOCK_CODE, default='', max_length=50)

    def __init__(self, *args, **kwargs):
        self.unique_keys = [ITEM_ID_COMPANY_ID, ITEM_ID_SERIAL_NUMBER]
        models.Model.__init__(self, *args, **kwargs)

    class Meta:
        db_table = TABLE_ID_COMPANY_LOGS
