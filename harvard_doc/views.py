from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from harvard_doc.models import *
from datetime import datetime, date, timedelta
from django.utils.timezone import utc
from django_xhtml2pdf import utils
import re

def html_view(request):
    dd = {}
    template = 'harvard_doc/index.html'
    return render_to_response(template, 
                              dd, 
                              context_instance=RequestContext(request))

def pdf_view(request):
    dd = {}
    template = 'harvard_doc/index_pdf.html'
    return utils.render_to_pdf_response(template, dd, name)
