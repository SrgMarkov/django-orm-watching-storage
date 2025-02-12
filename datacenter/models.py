from django.db import models
from django.utils import timezone
from datetime import timedelta


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def is_visit_long(self, minutes=60):
        if self.leaved_at is None:
            delta = timezone.now() - self.entered_at
        else:
            delta = self.leaved_at - self.entered_at
        return 'НЕТ' if delta <= timedelta(minutes=minutes) else 'ДА'

    def format_duration(self):
        delta = str(timezone.now() - self.entered_at).split(':')
        return f'{delta[0]}ч : {delta[1]}мин'

    def get_duration(self):
        delta = str(self.leaved_at - self.entered_at).split(':')
        return f'{delta[0]}ч : {delta[1]}мин'

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
