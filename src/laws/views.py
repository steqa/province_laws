from django.shortcuts import render

from .models import AdministrativeOffencesCodeChapter


def administrative_offences_code(request):
    chapters = AdministrativeOffencesCodeChapter.objects.prefetch_related().all()

    context = {'chapters': chapters}
    return render(request, 'laws/administrative_offences_code.html', context)