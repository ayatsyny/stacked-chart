from django.db import models


class DataSession(models.Model):
    session_key = models.BigIntegerField(primary_key=True)
    started_by = models.EmailField()
    created_at = models.DateTimeField()
    summary_status = models.CharField(max_length=50)
    duration = models.FloatField()
    worker_time = models.FloatField()
    bundle_time = models.PositiveIntegerField()
    num_workers = models.PositiveSmallIntegerField()
    branch = models.CharField(max_length=200)
    commit_id = models.CharField(max_length=200)
    started_tests_count = models.PositiveIntegerField(default=0)
    passed_tests_count = models.PositiveIntegerField()
    failed_tests_count = models.PositiveIntegerField()
    pending_tests_count = models.PositiveIntegerField()
    skipped_tests_count = models.PositiveIntegerField()
    error_tests_count = models.PositiveIntegerField()
