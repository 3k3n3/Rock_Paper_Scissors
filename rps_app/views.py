from django.shortcuts import render
from django.http import HttpResponse
from gameplay import gameplay


def home(request):
    return render(request, "rps_app/home.html")


def game(request):
    context = {}
    if request.method == "POST":
        x = request.POST.get("game")
        if x != None:
            # returning tuple (comp_move, decision, time_now, scoreboard)
            g = gameplay(x)
            context["y"] = g[0]
            context["z"] = g[1]
            context["t"] = g[2]
            context["sb"] = g[3]
        else:
            # send this as error message
            print("Form Submission Error!")
        context["x"] = x
    return render(request, "rps_app/game.html", context)


def friend(request):
    return HttpResponse(
        """
        <html>
        <style>
        div{
            background-color: blue;
            color: white
        }
        </style>
        <div style='outline: 1px solid red';>
        Hi ya
        </div>
        </html>
        """
    )
