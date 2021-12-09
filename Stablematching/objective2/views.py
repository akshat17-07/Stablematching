import random
from datetime import datetime
from . import NodeClass
from . import RandomMatch
from . import People
from . import *
from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request, "random.html")

def result(request):
    if request.method == "POST":
        form = request.POST
        num = form["num"]
        temp = People.People(int(num))

        output = temp.output()

        return render(request, "result.html", {
            "matches": output[0],
            "menMatches": output[1],
            "womenMatches": output[2]
        })


    else:
        return render(request, "random.html")
