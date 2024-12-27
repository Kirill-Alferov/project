from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")


def page(request):
    return render(request, "main/page.html")


def pagea(request):
    return render(request, "main/pagea.html")


def pageb(request):
    return render(request, "main/pageb.html")