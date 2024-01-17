from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    template = loader.get_template("threat_feed/index.html")
    context = {"latest_question_list": latest_question_list}
    return render(request, "threat_feed/index.html", context)
    return HttpResponse("Hello, world. You're at the Threat Feed Index Page.")