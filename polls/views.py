from django.shortcuts import render
from django.http import HttpResponse

from polls.services import question


def index(request):
    return HttpResponse("Hello, world.")

def question_view(request):
    try:
        resp = question.get_question()
        return HttpResponse([resp], status=200)

    except Exception as e:
        print("error: ", str(e))
        return HttpResponse("something not going well", status=500)

