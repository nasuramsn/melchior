from django.test import TestCase
from django.utils import timezone
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

    def test_get_master_with_uk(self):
        _company = Company()
        _company.company_id = "00001"
        _result = _company.get_with_uk()
        self.assertEqual(_result.serial_number, 1)
        self.assertEqual(_result.record.description, "こちらは会社の詳細の説明になります")
