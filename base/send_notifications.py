from django.core.management.base import BaseCommand
from base.models import Subscription
from django.utils import timezone

class Command(BaseCommand):
    help = 'Send notifications for events one day before'

    def handle(self, *args, **kwargs):
        one_day_away = timezone.now() + timezone.timedelta(days=1)
        events_to_notify = Subscription.objects.filter(event_date__date=one_day_away.date())

        for event in events_to_notify:
            print(f"Notifiction: {event.name} is tomorrow")