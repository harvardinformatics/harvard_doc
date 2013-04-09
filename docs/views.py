from django.shortcuts import render_to_response
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import logout
from django.template import RequestContext, loader, Context
from billing_record.models import *
from datetime import datetime, date, timedelta
from django.utils.timezone import utc
from django_xhtml2pdf import utils
import re

def index(request):
    dd = {}
    template = 'billing/index.html'
    return render_to_response('billing/index.html', 
                              dd, 
                              context_instance=RequestContext(request))

def pdf(request):
    dd = {}
    template = 'billing/index_pdf.html'
    return utils.render_to_pdf_response('billing/index_pdf.html', dd)
