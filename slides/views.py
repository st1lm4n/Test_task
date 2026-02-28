from django.shortcuts import render
from .models import Slide


def index(request):
    slides = Slide.objects.filter(is_active=True)
    return render(request, "slides/index.html", {"slides": slides})
