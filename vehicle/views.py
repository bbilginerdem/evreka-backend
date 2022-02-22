from datetime import timedelta

from django.utils import timezone

from django.shortcuts import render
from .models import NavigationRecord


def get_48_hours(request):

    time_48 = timezone.now() - timedelta(hours=48)
    results = NavigationRecord.objects.filter(datetime__gte=time_48)
    context = {

            'results': results,
    }

    return render(request, 'output.html', context)
