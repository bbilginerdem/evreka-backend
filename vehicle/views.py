from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from .models import NavigationRecord


def get_48_hours(request):
    time_48 = timezone.now() - timedelta(hours=48)
    response = NavigationRecord.objects.filter(datetime__gte=time_48).order_by('vehicle', 'datetime').distinct('vehicle')
    context = {

        'response': response,
    }

    return render(request, 'output.html', context)
