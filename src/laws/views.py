from django.shortcuts import render

from .models import AdministrativeOffencesCodeChapter, CriminalCodeChapter


def main(request):
    administrative_offences_code = AdministrativeOffencesCodeChapter.objects.all()
    criminal_code = CriminalCodeChapter.objects.all()

    context = {
        'administrative_offences_code': administrative_offences_code,
        'criminal_code': criminal_code,
    }

    return render(request, 'laws/main.html', context)
