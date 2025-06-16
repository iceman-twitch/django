from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Category
from .models import Image
from .models import Video

import requests
import json
from datetime import datetime
import re

# Create your views here.
def index( request ):

    category = get_object_or_404(Category, pk=1)

    all_obj = Category.objects.all()
    #all_img = Image.objects.get(pk=id)
    all_img = Image.objects.filter( category=1 )
    #all_img = Image.objects.get(pk=id)

    categorys = { 'category_title' : category.title, 'categorys' : all_obj, 'images' : all_img }

    return render( request, 'frontend/index.html', categorys )

def detail( request, id ):

    category = get_object_or_404(Category, pk=id)

    all_obj = Category.objects.all()
    #all_img = Image.objects.get(pk=id)
    all_img = Image.objects.filter( category=id )
    #all_img = Image.objects.get(pk=id)

    categorys = { 'category_title' : category.title, 'categorys' : all_obj, 'images' : all_img }

    return render( request, 'frontend/index.html', categorys )
    