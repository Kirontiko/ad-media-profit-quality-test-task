from django.urls import path

from revenue.views import RevenueStatisticsView

urlpatterns = [
    path('revenue-statistics/', RevenueStatisticsView.as_view(), name='revenue-statistics'),
]

app_name = "revenue-statistic"
