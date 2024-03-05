"""
Django Command to wait for db to be available (runnable from manage.py)
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        pass
