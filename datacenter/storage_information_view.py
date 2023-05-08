from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    non_closed_visits = []
    entered = Visit.objects.filter(leaved_at=None)
    for person in range(len(entered)):
        person_dict = {'who_entered': entered[person].passcard,
                       'entered_at': timezone.localtime(entered[person].entered_at),
                       'duration': Visit.format_duration(entered[person]),
                       'is_strange': Visit.is_visit_long(entered[person])}
        non_closed_visits.append(person_dict)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
