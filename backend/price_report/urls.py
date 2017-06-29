from django.conf.urls import url
from price_report import views

urlpatterns = [
    url(r'^price_report/create/$', views.PriceReportCreate.as_view()),
    url(r'^price_report/(?P<pk>[0-9]+)$', views.PriceReportDetail.as_view()),
    url(r'^price_report/$', views.PriceReportList.as_view()),
]