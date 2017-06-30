from django.test import TestCase

from price_report.models import PriceReport

class PriceReportModelTest(TestCase):
    """
    Test the Price Report Model
    """

    @classmethod
    def setUpTestData(cls):
        # Create two price reports
        PriceReport.objects.create(latitude=30.2672, longitude=-97.7431, price=2.46, octane_rating=90) # Austin, TX
        PriceReport.objects.create(latitude=47.6062, longitude=-122.3321, price=12.36, octane_rating=118) # Seattle, WA
