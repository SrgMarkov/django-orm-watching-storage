from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    non_closed_visits = []
    active_visitors = Visit.objects.filter(leaved_at=None)
    for visitor in active_visitors:
        person_dict = {'who_entered': visitor.passcard,
                       'entered_at': timezone.localtime(visitor.entered_at),
                       'duration': Visit.format_duration(visitor),
                       'is_strange': Visit.is_visit_long(visitor)}
        non_closed_visits.append(person_dict)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
