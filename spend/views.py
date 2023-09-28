from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView

from spend.models import SpendStatistic


class SpendStatisticsView(APIView):
    def get(self, request):
        spend_statistic = SpendStatistic.objects.values(
            "name", "date"
        ).annotate(
            total_spend=Sum("spend"),
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversions=Sum("conversion"),
            total_revenue=Sum("revenuestatistic__revenue"))

        result_data = list(spend_statistic)
        return Response(result_data)
