from django.shortcuts import render

from .models import AdministrativeOffencesCodeChapter, CriminalCodeChapter


def administrative_offences_code(request):
    chapters = AdministrativeOffencesCodeChapter.objects.prefetch_related().all()

    context = {'chapters': chapters}
    return render(request, 'laws/administrative_offences_code.html', context)


def criminal_code(request):
    chapters = CriminalCodeChapter.objects.prefetch_related().all()

    context = {'chapters': chapters}
    return render(request, 'laws/criminal_code.html', context)