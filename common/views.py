from django.shortcuts import render
from common.models import Comment


def landing_page(req):
    return render(req, 'landing_page.html')
