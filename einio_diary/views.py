from django.shortcuts import render
from einio_diary.models import Irasas

def home(request):

    context_dict = {}
    context_dict["irasai"] = Irasas.objects.all()
    return render(request, "home.html", context_dict)
