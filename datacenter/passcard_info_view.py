from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    employee_visits = Visit.objects.filter(passcard=passcard)
    for visit in employee_visits:
        pass_dict = {
            'entered_at': visit.entered_at,
            'duration': Visit.get_duration(visit),
            'is_strange': Visit.is_visit_long(visit)}
        this_passcard_visits.append(pass_dict)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
