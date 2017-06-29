from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('price_report.urls')),
]
