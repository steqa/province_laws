from django.http.response import JsonResponse
from django.shortcuts import render

from .models import (AdministrativeOffencesCode,
                     AdministrativeOffencesCodeChapter, CriminalCode,
                     CriminalCodeChapter)
from .utils import form_response


def main(request):
    return render(request, 'laws/main.html')


def get_administrative_offences_code(request):
    administrative_offences_code_chapter = AdministrativeOffencesCodeChapter.objects.all().order_by('number')
    administrative_offences_code = AdministrativeOffencesCode.objects.all().order_by('chapter', 'number')
    response = form_response(administrative_offences_code_chapter, administrative_offences_code)
    return JsonResponse(response, safe=False)


def get_criminal_code(request):
    criminal_code_chapter = CriminalCodeChapter.objects.all().order_by('number')
    criminal_code = CriminalCode.objects.all().order_by('chapter', 'number')
    response = form_response(criminal_code_chapter, criminal_code)
    return JsonResponse(response, safe=False)