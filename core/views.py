from django.shortcuts import render
from django.utils import timezone


def home(request):
    """Landing page that explains what Footprint is."""
    return render(request, "core/home.html")


def ping(request):
    """Small HTMX demo: returns a piece of HTML, not a whole page."""
    return render(request, "core/partials/ping.html", {"now": timezone.localtime()})
