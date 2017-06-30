from price_report.models import PriceReport
from price_report.serializers import PriceReportSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

import datetime


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
        """
        Override APIView 'get' method to retrieve list based on start/end timeframe specification
        TODO: Encapsulate filtering w/ custom Django Filter
        """
        queryset = PriceReport.objects.all()

        start_timestamp = request.query_params.get('start_date', None)
        end_timestamp = request.query_params.get('end_date', None)

        if start_timestamp is None or end_timestamp is None:
            return Response({
                'reason': 'start_date and/or end_date query parameters not present'
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Attempt to unpackage dates from query param strings
            try:
                start_date = datetime.datetime.strptime(start_timestamp, '%Y-%m-%d')
                end_date = datetime.datetime.strptime(end_timestamp, '%Y-%m-%d')
            except ValueError:
                return Response({
                    'reason': 'dates must be formatted YYYY-MM-DD in query parameters'
                })

        filtered = queryset.filter(submitted__gte=start_date) \
                           .filter(submitted__lte=end_date)
        serializer = PriceReportSerializer(filtered, many=True)
        return Response(data=serializer.data)
