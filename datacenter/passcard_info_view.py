from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.http import Http404


def passcard_info_view(request, passcode):
    try:
        passcard = Passcard.objects.get(passcode=passcode)
        this_passcard_visits = []
        person_vizit = Visit.objects.filter(passcard=passcard)
        for enter in range(len(person_vizit)):
            pass_dict = {
                'entered_at': person_vizit[enter].entered_at,
                'duration': Visit.get_duration(person_vizit[enter]),
                'is_strange': Visit.is_visit_long(person_vizit[enter])}
            this_passcard_visits.append(pass_dict)

        context = {
            'passcard': passcard,
            'this_passcard_visits': this_passcard_visits
        }
        return render(request, 'passcard_info.html', context)
    except Passcard.DoesNotExist:
        raise Http404()
