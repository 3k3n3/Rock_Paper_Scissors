from django.shortcuts import render
from django.http import HttpResponse
from gameplay import gameplay

def game(request):
    context = {}
    if request.method == "POST":
        x = request.POST.get("game")
        if x != None:
            # returning tuple (comp_move, decision, time_now, delay)
            g = gameplay(x)
            context["y"] = g[0]
            context["z"] = g[1]
            context["t"] = g[2]
        context["x"] = x
    return render(request, "rps_app/game.html", context)