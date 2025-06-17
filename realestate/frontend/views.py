from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader
from django.utils.translation import activate, get_language_info

import requests
import json
from datetime import datetime
import re

def index( request ):
    
    return render( request, 'frontend/index.html' )
    # return HttpResponse( 'Current Language: ' + request.LANGUAGE_CODE )


def handler404(request, exception, template_name="frontend/index.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def page_not_found_view( request, exception ):
    #context = RequestContext(request)
    #context['posts'] = Post.objects.all()
    #return render_to_response(myapp/404.html, context.flatten())
    return render( request, 'frontend/index.html' )

def handler500(request, *args, **argv):
    return render( request, 'frontend/index.html', status=500 )