from datetime import datetime
from django.db import models

from ..consts.ErrorMessages import ERROR_MESSAGE_VALIDATION_00001
from ..consts.ItemNames import ITEM_NAME_CREATED_AT, ITEM_NAME_CREATED_BY, ITEM_NAME_SERIAL_NUMNBER, \
    ITEM_NAME_STATUS, ITEM_NAME_UPDATED_AT, ITEM_NAME_UPDATED_BY
from ..exceptions.CoreExceptions import CoreModelException

import logging

logger = logging.getLogger('django')


class CoreModel(models.Model):

    # id = models.BigIntegerField(
    #    verbose_name=ITEM_NAME_ID, default=0, max_length=18)
    serial_number = models.BigIntegerField(
        verbose_name=ITEM_NAME_SERIAL_NUMNBER, default=0)
    unique_keys = []
    alias = ""
    created_at = models.DateTimeField(
        verbose_name=ITEM_NAME_CREATED_AT, auto_now=True)
    created_by = models.CharField(
        verbose_name=ITEM_NAME_CREATED_BY, default='', max_length=50)

    # search db record with unique keys
    def get_with_uk(self):

        if len(self.unique_keys) == 0:
            raise CoreModelException(
                ERROR_MESSAGE_VALIDATION_00001 % 'unique keys')

        _key_values = {}
        for key, value in self.__dict__.items():
            if callable(value) is False:
                if key != '_state' and key != 'unique_keys':
                    if key in self.unique_keys:
                        _key_values[key] = value

        _results = self.__class__.objects.get(**_key_values)

        return _results

    def __str__(self):

        _results = ''
        for key, value in self.__dict__.items():
            if callable(value) is False:
                _type = type(value)
                _value = ''
                if _type == models.DateTimeField:
                    # _value = datetime.strftime("%Y-%m-%d %H:%M:%S")
                    _value = datetime.strftime()
                else:
                    _value = value
                _results = _results + "{" + str(key) + ":" + str(_value) + "},"

        return "[" + _results[:len(_results) - 1] + "]"

    class Meta:
        abstract = True
        managed = False


class CoreMaster(CoreModel):

    updated_at = models.DateTimeField(
        verbose_name=ITEM_NAME_UPDATED_AT, auto_now=True)
    updated_by = models.CharField(
        verbose_name=ITEM_NAME_UPDATED_BY, default='', max_length=50)
    status = models.IntegerField(
        verbose_name=ITEM_NAME_STATUS, default=0)
    record = None

    class Meta:
        abstract = True
        managed = False


class CoreRecord(CoreModel):

    class Meta:
        abstract = True
        managed = False
