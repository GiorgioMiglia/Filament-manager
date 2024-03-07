from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Filament, Comment
from django.views import generic


def index(request):
    filament_list = Filament.objects.all()
    context = {"filament_list": filament_list}
    return render(request, "filamentManager/index.html", context)

def detail(request, filament_id):
    filament = get_object_or_404(Filament, pk=filament_id)
    return render(request, "filamentManager/detail.html", {"filament": filament})

def add_comment(request, filament_id):
    filament = get_object_or_404(Filament, pk=filament_id)
    comment_text = request.POST.get('comment_text')
    if comment_text:
        comment = Comment.objects.create(Filament=filament, comment_text=comment_text)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))