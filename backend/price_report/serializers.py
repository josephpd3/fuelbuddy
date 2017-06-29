from rest_framework import serializers
from price_report.models import PriceReport


class PriceReportSerializer(serializers.ModelSerializer):
    """
    Serializer for the PriceReport model
    """
    class Meta:
        model = PriceReport
        fields = ('id', 'submitted', 'latitude', 'longitude', 'price', 'octane_rating')
