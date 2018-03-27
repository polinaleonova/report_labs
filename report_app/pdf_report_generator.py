# -*- coding: utf-8 -*-
import django
from django.template.loader import render_to_string
import pdfkit
import json

options = {
    'javascript-delay': '2000',
    'page-size': 'Letter',
    'margin-top': '2px',
    'margin-right': '2px',
    'margin-bottom': '2px',
    'margin-left': '2px',
    'encoding': "UTF-8"
}


def generate_pdf(path_to_json):
    with open(path_to_json, 'r') as data_file:
        context = json.load(data_file)

    rendered = render_to_string('template_by_word.html', context)

    # Generate PDF from string.
    # pdfkit.from_string(rendered, 'out.pdf', options=options)
    # print('pdf ready')
    return rendered