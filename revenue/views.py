from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView

from revenue.models import RevenueStatistic


class RevenueStatisticsView(APIView):
    def get(self, request):
        revenue_data = RevenueStatistic.objects.values('name', 'date').annotate(
            total_revenue=Sum('revenue'),
        )

        revenue_data = revenue_data.annotate(
            total_spend=Sum('spend__spend'),
            total_impressions=Sum('spend__impressions'),
            total_clicks=Sum('spend__clicks'),
            total_conversion=Sum('spend__conversion')
        )

        result_data = []
        for item in revenue_data:
            result_data.append({
                'name': item['name'],
                'date': item['date'],
                'total_revenue': item['total_revenue'],
                'total_spend': item['total_spend'],
                'total_impressions': item['total_impressions'],
                'total_clicks': item['total_clicks'],
                'total_conversion': item['total_conversion'],
            })

        return Response(result_data)
