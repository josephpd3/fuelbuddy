from django.test import TestCase

from price_report.models import PriceReport

class PriceReportModelTest(TestCase):
    """
    """

    @classmethod
    def setUpTestData(cls):
        PriceReport.objects.create(latitude=46.9, longitude=36.7, price=2.46, octane_rating=12)
