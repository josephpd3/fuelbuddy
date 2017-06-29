from price_report.models import PriceReport
from price_report.serializers import PriceReportSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics


class PriceReportCreate(generics.CreateAPIView):
    """
    Generic creation endpoint for price reports
    """
    queryset = PriceReport.objects.all()
    serializer_class = PriceReportSerializer


class PriceReportDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic endpoint for retrieving, updating, and destroying price reports via ID
    """
    queryset = PriceReport.objects.all()
    serializer_class = PriceReportSerializer


class PriceReportList(APIView):
    """
    Endpoint for retrieving a list of Price Reports
    """
    def get(self, request, format=None):
        raise NotImplementedError
