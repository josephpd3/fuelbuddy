from django.db import models


class PriceReport(models.Model):
    """
    Model which tracks a fuel price report by location, price, and octane rating
    """
    submitted = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6) # TODO: Add PostGIS support to utilize a single PointField
    longitude = models.DecimalField(max_digits=9, decimal_places=6) # ...instead of these two DecimalFields
    price = models.DecimalField(max_digits=8, decimal_places=2)
    octane_rating = models.IntegerField() # TODO: Add validation bounds to this field. IE: 0 < 130 as range for values
