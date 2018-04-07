import os

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .pdf_report_generator import generate_pdf


def generate_pdf_report(request):
    # generate_pdf(os.path.join(settings.MEDIA_ROOT, 'JSON.json'))

    return HttpResponse(generate_pdf(os.path.join(settings.MEDIA_ROOT, 'JSON.json')))