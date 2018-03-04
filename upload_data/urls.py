from django.conf.urls import url
from .views import StatusDays, DurationDays, DetailStatus

urlpatterns = [
    url(r'^status-per-day/$',  StatusDays.as_view(), name='status_all_days'),
    url(r'^detail-status-per-day/$',  DetailStatus.as_view(), name='detail_status_all_days'),
    url(r'^duration-and-days/$', DurationDays.as_view(),  name='duration_vs_days'),
]
