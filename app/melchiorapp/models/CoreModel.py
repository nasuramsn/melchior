from datetime import datetime
from django.db import models

from ..consts.ItemIds import ITEM_ID_SERIAL_NUMBER
from ..consts.ItemNames import ITEM_NAME_CREATED_AT, ITEM_NAME_CREATED_BY, ITEM_NAME_SERIAL_NUMNBER, \
    ITEM_NAME_STATUS, ITEM_NAME_UPDATED_AT, ITEM_NAME_UPDATED_BY
from ..exceptions.CoreExceptions import CoreModelException
from ..messages.ErrorMessages import ERROR_MESSAGE_DATA_00001, ERROR_MESSAGE_DATA_00002, \
    ERROR_MESSAGE_VALIDATION_00001, ERROR_MESSAGE_VALIDATION_00002

import copy
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

    def create_key_values(self, keys):

        _key_values = {}
        for key, value in self.__dict__.items():
            if callable(value) is False:
                if key != '_state' and key != 'unique_keys':
                    if key in keys:
                        _key_values[key] = value

        return _key_values

    # search db record with unique keys
    def get_with_uk(self):

        if len(self.unique_keys) == 0:
            raise CoreModelException(
                ERROR_MESSAGE_VALIDATION_00001 % 'unique keys')

        _key_values = self.create_key_values(self.unique_keys)
        _results = self.__class__.objects.get(**_key_values)

        return _results

    # search db record with unique keys(without serial_number)
    def get_with_keys(self):

        _check_keys = copy.deepcopy(self.unique_keys)
        if ITEM_ID_SERIAL_NUMBER in _check_keys:
            _check_keys.remove(ITEM_ID_SERIAL_NUMBER)

        _key_values = self.create_key_values(_check_keys)
        _results = self.__class__.objects.filter(**_key_values)

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

    def check_master_record_keys(self):

        _record_keys = copy.deepcopy(self.record.unique_keys)
        _master_key_values = self.create_key_values(self.unique_keys)
        _record_key_values = self.record.create_key_values(_record_keys)
        for key, value in _master_key_values.items():
            _record_value = _record_key_values[key]
            if value != _record_value:
                raise CoreModelException(
                    ERROR_MESSAGE_VALIDATION_00002 % (value, _record_value))

    def create_with_record(self):

        if self.record is None:
            raise CoreModelException(
                ERROR_MESSAGE_VALIDATION_00001 % 'record')

        # check unique keys of master and record
        self.check_master_record_keys()

        # check record is already exists
        _check = self.get_with_keys()
        if len(_check) > 0:
            raise CoreModelException(
                ERROR_MESSAGE_DATA_00001 % str(self.create_key_values(self.unique_keys)))

        _record = self.record.create_record()
        self.serial_number = _record.serial_number
        self.full_clean()
        self.save()

        return self

    def update_with_record(self):

        if self.record is None:
            raise CoreModelException(
                ERROR_MESSAGE_VALIDATION_00001 % 'record')

        # check unique keys of master and record
        self.check_master_record_keys()

        # check record is already exists
        _check = self.get_with_keys()
        if len(_check) == 0:
            raise CoreModelException(
                ERROR_MESSAGE_DATA_00002 % str(self.create_key_values(self.unique_keys)))

        _record = self.record.create_record()
        self.serial_number = _record.serial_number
        self.full_clean()
        self.save()

    def delete_master(self):

        if self.record is None:
            raise CoreModelException(
                ERROR_MESSAGE_VALIDATION_00001 % 'record')

        # check unique keys of master and record
        self.check_master_record_keys()

        # check record is already exists
        _check = self.get_with_keys()
        if len(_check) == 0:
            raise CoreModelException(
                ERROR_MESSAGE_DATA_00002 % str(self.create_key_values(self.unique_keys)))

        self.status = 0
        self.save()

    class Meta:
        abstract = True
        managed = False


class CoreRecord(CoreModel):

    def create_record(self):

        # check last serial_number
        _records = self.get_with_keys()
        if _records is None or len(_records) == 0:
            self.serial_number = 1
        else:
            _last_record = _records.order_by(
                ITEM_ID_SERIAL_NUMBER).reverse().first()
            self.serial_number = _last_record.serial_number + 1
        self.full_clean()
        self.save()

        return self

    class Meta:
        abstract = True
        managed = False
