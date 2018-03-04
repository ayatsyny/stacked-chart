import os
import csv
from django.core.management.base import BaseCommand, CommandError
from upload_data.models import DataSession


class Command(BaseCommand):
    args = '<file_name.csv>'
    help = 'Import format file [*.csv]'

    def add_arguments(self, parser):
        parser.add_argument('path_file', type=str, help='path_file.csv')

    def handle(self, *args, **options):
        if not options.get('path_file'):
            raise CommandError('You need only path file')
        extension = os.path.splitext(options['path_file'])[1]
        if extension != '.csv':
            raise CommandError("Format doesn't support")
        with open(os.path.abspath(options['path_file'])) as csvfile:
            reader = csv.DictReader(csvfile)
            objects = []
            for row in reader:
                created_at = row['created_at'][:-4]
                obj = DataSession(session_key=row['session_id'], started_by=row['started_by'],
                                  created_at=created_at,
                                  summary_status=row['summary_status'], duration=row['duration'],
                                  worker_time=row['worker_time'], bundle_time=row['bundle_time'],
                                  num_workers=row['num_workers'], branch=row['branch'],
                                  commit_id=row['commit_id'],
                                  started_tests_count=row['started_tests_count'],
                                  passed_tests_count=row['passed_tests_count'],
                                  failed_tests_count=row['failed_tests_count'],
                                  pending_tests_count=row['pending_tests_count'],
                                  skipped_tests_count=row['skipped_tests_count'],
                                  error_tests_count=row['error_tests_count'])
                objects.append(obj)
            DataSession.objects.bulk_create(objects)
            self.stdout.write(self.style.SUCCESS('Successfully create objects: {}'.format(DataSession.objects.count())))
