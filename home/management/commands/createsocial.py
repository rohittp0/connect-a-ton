import os

from django.core.management.base import BaseCommand
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site


class Command(BaseCommand):
    help = 'Creates a Google social app for allauth'

    def handle(self, *args, **kwargs):
        site = Site.objects.get_current()
        social_app, created = SocialApp.objects.get_or_create(
            provider='google',
            name='Google',
            client_id=os.environ.get('GOOGLE_OAUTH2_CLIENT_ID'),
            secret=os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET'),
        )
        social_app.sites.add(site)
