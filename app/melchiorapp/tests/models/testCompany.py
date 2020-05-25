from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from ...exceptions.CoreExceptions import CoreModelException
from ...messages.ErrorMessages import ERROR_MESSAGE_DATA_00001, ERROR_MESSAGE_VALIDATION_00002
from ...models.Company import Company, CompanyLog


class CompanyTestCase(TestCase):

    def setUp(self):
        CompanyLog.objects.create(
            company_id="00001",
            serial_number=1,
            name="TEST用会社",
            post_code="111-1111",
            address1="東京都港区品川１－１－１",
            address2="神奈川県川崎市川崎区駅前本町１－１－１",
            tel_no="000-0000-0000",
            email_address1="test1@test.melchior",
            email_address2="test2@test.melchior",
            homepage_url="https://testhomepage.melchior.com/",
            founded_at="2020-05-05",
            president="田中一郎",
            summary="テストに使用する会社です。",
            description="こちらは会社の詳細の説明になります",
            market_code="00001",
            stock_code="1234",
            created_at=timezone.now(),
            created_by="system"
        )

        Company.objects.create(
            serial_number=1,
            created_at=timezone.now(),
            created_by="system",
            updated_at=timezone.now(),
            updated_by="system",
            status=1,
            company_id="00001"
        )

    def test_create_master_with_record(self):

        _company = Company()
        _company.company_id = "00002"
        _company.created_at = timezone.now()
        _company.created_by = "system"
        _company.updated_at = timezone.now()
        _company.updated_by = "system"
        _company.status = 1

        _company_log = CompanyLog()
        _company_log.company_id = "00002"
        _company_log.name = "TEST用会社2"
        _company_log.post_code = "111-1112"
        _company_log.address1 = "東京都港区品川１－１－2"
        _company_log.address2 = "神奈川県川崎市川崎区駅前本町１－１－2"
        _company_log.tel_no = "000-0000-0001"
        _company_log.email_address1 = "test1@test.melchior2"
        _company_log.email_address2 = "test2@test.melchior2"
        _company_log.homepage_url = "https://testhomepage.melchior.com/"
        _company_log.founded_at = "2020-05-06"
        _company_log.president = "鈴木一郎"
        _company_log.summary = "テストに使用する会社です2。"
        _company_log.description = "こちらは会社の詳細の説明になります2"
        _company_log.market_code = "00001"
        _company_log.stock_code = "1234"
        _company_log.created_at = timezone.now()
        _company_log.created_by = "system"

        _company.record = _company_log
        _company.create_with_record()

        _check_company = Company()
        _check_company.company_id = "00002"
        _result = _check_company.get_with_uk()
        self.assertEqual(_result.serial_number, 1)
        self.assertEqual(_result.record.description, "こちらは会社の詳細の説明になります2")

    def test_create_master_with_no_record(self):

        _company = Company()
        _company.company_id = "00003"
        _company.created_at = timezone.now()
        _company.created_by = "system"
        _company.updated_at = timezone.now()
        _company.updated_by = "system"
        _company.status = 1

        _company_log = CompanyLog()
        _company_log.company_id = "10003"
        _company_log.name = "TEST用会社2"
        _company_log.post_code = "111-1112"
        _company_log.address1 = "東京都港区品川１－１－2"
        _company_log.address2 = "神奈川県川崎市川崎区駅前本町１－１－2"
        _company_log.tel_no = "000-0000-0001"
        _company_log.email_address1 = "test1@test.melchior2"
        _company_log.email_address2 = "test2@test.melchior2"
        _company_log.homepage_url = "https://testhomepage.melchior.com/"
        _company_log.founded_at = "2020-05-06"
        _company_log.president = "鈴木一郎"
        _company_log.summary = "テストに使用する会社です2。"
        _company_log.description = "こちらは会社の詳細の説明になります2"
        _company_log.market_code = "00001"
        _company_log.stock_code = "1234"
        _company_log.created_at = timezone.now()
        _company_log.created_by = "system"

        _company.record = _company_log

        with self.assertRaisesMessage(CoreModelException, ERROR_MESSAGE_VALIDATION_00002 % ("00003", "10003")):
            _company.create_with_record()

    def test_create_master_with_record_already_exists(self):

        _company = Company()
        _company.company_id = "00001"
        _company.created_at = timezone.now()
        _company.created_by = "system"
        _company.updated_at = timezone.now()
        _company.updated_by = "system"
        _company.status = 1

        _company_log = CompanyLog()
        _company_log.company_id = "00001"
        _company_log.name = "TEST用会社3"
        _company_log.post_code = "111-1113"
        _company_log.address1 = "東京都港区品川１－１－３"
        _company_log.address2 = "神奈川県川崎市川崎区駅前本町１－１－３"
        _company_log.tel_no = "000-0000-0003"
        _company_log.email_address1 = "test1@test.melchior3"
        _company_log.email_address2 = "test2@test.melchior3"
        _company_log.homepage_url = "https://testhomepage.melchior.com/"
        _company_log.founded_at = "2020-05-25"
        _company_log.president = "佐藤試験"
        _company_log.summary = "テストに使用する会社です2。"
        _company_log.description = "こちらは会社の詳細の説明になります2"
        _company_log.market_code = "00003"
        _company_log.stock_code = "1234"
        _company_log.created_at = timezone.now()
        _company_log.created_by = "system"

        _company.record = _company_log

        with self.assertRaisesMessage(CoreModelException, ERROR_MESSAGE_DATA_00001 % "{'company_id': '00001'}"):
            _company.create_with_record()

    def test_create_master_with_record_format_check(self):

        _company = Company()
        _company.company_id = "00004"
        _company.created_at = timezone.now()
        _company.created_by = "system"
        _company.updated_at = "い"
        _company.updated_by = "system"
        _company.status = 1

        _company_log = CompanyLog()
        _company_log.company_id = "00004"
        _company_log.name = "TEST用会社4"
        _company_log.post_code = "111-1114"
        _company_log.address1 = "東京都港区品川１－１－４"
        _company_log.address2 = "神奈川県川崎市川崎区駅前本町１－１－４"
        _company_log.tel_no = "000-0000-0004"
        _company_log.email_address1 = "test1@test.melchior4"
        _company_log.email_address2 = "test2@test.melchior4"
        _company_log.homepage_url = "https://testhomepage.melchior.com/"
        _company_log.founded_at = "2020-05-26"
        _company_log.president = "田井中テスト"
        _company_log.summary = "テストに使用する会社です4。"
        _company_log.description = "こちらは会社の詳細の説明になります4"
        _company_log.market_code = "00004"
        _company_log.stock_code = "1234"
        _company_log.created_at = "あ"
        _company_log.created_by = "system"

        _company.record = _company_log

        with self.assertRaisesMessage(ValidationError, "{'created_at': ['“あ” value has an invalid format. It must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format.']}"):
            _company.create_with_record()

    def test_get_master_with_uk(self):

        _company = Company()
        _company.company_id = "00001"
        _result = _company.get_with_uk()
        self.assertEqual(_result.serial_number, 1)
        self.assertEqual(_result.record.description, "こちらは会社の詳細の説明になります")

    def test_update_record(self):

        _company = Company()
        _company.company_id = "00001"
        _origin = _company.get_with_uk()
        _origin.record.summary = "概要を修正します"
        _origin.update_with_record()

        _company_search = Company()
        _company_search.company_id = "00001"
        _company_search = _company.get_with_uk()
        self.assertEqual(_company_search.serial_number, 2)
        self.assertEqual(_company_search.record.summary, "概要を修正します")

    def test_delete_record(self):

        _company = Company()
        _company.company_id = "00001"
        _origin = _company.get_with_uk()
        _origin.delete_master()

        _company_search = Company()
        _company_search.company_id = "00001"
        _company_search = _company.get_with_uk()
        self.assertEqual(_company_search.status, 0)
