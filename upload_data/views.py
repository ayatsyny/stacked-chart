from chartit import PivotDataPool, PivotChart, DataPool, Chart
from django.db.models import Max, Count
from django.views.generic import TemplateView
from .models import DataSession


class StatusDays(TemplateView):
    template_name = 'upload_data/status_all_day.html'

    def data_chart_cicle(self):
        ds = DataPool(
            series=[{
                'options': {
                    'source': DataSession.objects.values('summary_status',).annotate(count=Count('summary_status')),
                },
                'terms': [
                    'summary_status',
                    'count',
                ]
            }]
        )
        cht = Chart(
            datasource=ds,
            series_options=[{
                'options': {
                    'type': 'pie',
                    'stacking': False
                },
                'terms': {
                    'summary_status': ['count']
                }
            }],
            chart_options={
                'title': {
                    'text': 'Summary status all days'
                }
            },
        )
        return cht

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rainpivchart'] = self.data_chart_cicle()
        return context


class DurationDays(TemplateView):
    template_name = 'upload_data/duration_days.html'

    def data_chart(self):
        ds = PivotDataPool(
            series=[{
                'options': {
                    'source': DataSession.objects.all(),
                    'categories': 'created_at',
                },
                'terms': {
                    'duration': Max('duration'),
                }
            }]
        )

        pivcht = PivotChart(
            datasource=ds,
            series_options=[{
                'options': {
                    'type': 'column',
                    'stacking': True,
                    'xAxis': 0,
                    'yAxis': 0,
                },
                'terms': ['duration']
            }],
            chart_options={
                'title': {
                    'text': 'Duration and datetime'
                },
                'xAxis': {
                    'labels':
                        {'step': 3, 'rotation': 90, 'align': 'bottom'},
                },
                'yAxis': {
                    'title': {
                        'text': 'Duration'
                    }
                }
            }
        )

        return pivcht

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rainpivchart'] = self.data_chart()
        return context


class DetailStatus(TemplateView):
    template_name = 'upload_data/detail_status_days.html'

    def detail_chart(self):
        ds = DataPool(
            series=[
                {'options': {
                    'source': DataSession.objects.all(),
                },
                'terms': [
                    'created_at',
                    'passed_tests_count',
                    'failed_tests_count',
                    'pending_tests_count',
                    'skipped_tests_count',
                    'error_tests_count',
                ],
        }])

        pivcht = Chart(
            datasource=ds,
            series_options=[{
                'options': {
                    'type': 'column',
                    'stacking': True,
                    'yAxis': 0},
                'terms': {
                    'created_at': [
                        'passed_tests_count',
                        'failed_tests_count',
                        'pending_tests_count',
                        'skipped_tests_count',
                        'error_tests_count',
                    ]
                }
                }],
            chart_options={
                'title': {
                    'text': 'Detail status tests'
                },
                'xAxis': {
                    'labels':
                        {'step': 3, 'rotation': 90, 'align': 'bottom'},
                },
                'yAxis': {
                    'title': {
                        'text': 'Tests'
                    }
                }
            }
        )
        return pivcht

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rainpivchart'] = self.detail_chart()
        return context
