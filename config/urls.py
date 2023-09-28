from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/revenue_statistic/', include("revenue.urls", namespace="revenue-statistic")),
    path('api/v1/spend_statistic/', include("spend.urls", namespace="spend-statistic"))
]
