from django.test import TestCase
from price_report.models import PriceReport

from django.core.urlresolvers import reverse

import datetime


class PriceReportViewTest(TestCase):
    """
    Unit tests for Price Report Views

    TODO: Get, Update
    """

    @classmethod
    def setUpTestData(cls):
        # Create two price reports
        PriceReport.objects.create(latitude=30.2672, longitude=-97.7431, price=2.46, octane_rating=90) # Austin, TX
        PriceReport.objects.create(latitude=47.6062, longitude=-122.3321, price=12.36, octane_rating=118) # Seattle, WA

    def test_list_reports_between_dates(self):
        """
        Tests Price Report list endpoint by grabbing test objects inserted between yesterday and tomorrow
        """
        today = datetime.datetime.now()
        one_day = datetime.timedelta(days=1)
        yesterday, tomorrow = today - one_day, today + one_day

        response = self.client.get('/price_report/?start_date={}&end_date={}'.format(
            yesterday.strftime('%Y-%m-%d'),
            tomorrow.strftime('%Y-%m-%d')
        ))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_create_report(self):
        """
        Tests creation of a Price Report via the /add/ endpoint
        """
        response = self.client.post('/price_report/add/', {
            'latitude': 30.2672,
            'longitude': 97.7431,
            'price': 3.12,
            'octane_rating': 96
        })
        self.assertEqual(response.status_code, 201)

    def test_delete_report(self):
        """
        Tests deletion of a Price Report
        """
        # create report
        response = self.client.post('/price_report/add/', {
            'latitude': 30.2672,
            'longitude': 97.7431,
            'price': 3.12,
            'octane_rating': 96
        })

        # See if it deletes
        report_id = response.data['id']
        response = self.client.delete('/price_report/{}'.format(report_id))
        self.assertEqual(response.status_code, 204)
