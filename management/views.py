from django.shortcuts import render
from .models import Color
from .forms import ColorForm, SearchColorForm


# Create your views here.
def index(request):
    colors = {}
    searchName = ""
    if request.method == "POST":
        searchForm = SearchColorForm(request.POST)
        if searchForm.is_valid():
            searchName = searchForm.cleaned_data['name']
            colors = Color.objects.filter(name__icontains=searchName)
            searchForm = SearchColorForm()
    else:
        colors = Color.objects.all()
        searchForm = SearchColorForm()
    new_color_id = Color.objects.last().id + 1
    return render(request, 'management/colors.html', context={'colors': colors, 'searchForm': searchForm,
                                                              'searchName': searchName, 'new_color_id': new_color_id})


def color_details(request, color_id):
    if request.method == "POST":
        color = Color.objects.get(pk=color_id)
        colorForm = ColorForm(request.POST, instance=color)
        if colorForm.is_valid():
            colorForm.save(commit=True)
            return render(request, 'management/color_details.html', context={'color': color, 'colorForm': colorForm})
    else:
        if color_id not in [color.pk for color in Color.objects.all()]:
            color = Color(pk=color_id, name="Nuovo colore", red=0, green=0, blue=0)
            color.save()
        else:
            color = Color.objects.get(pk=color_id)
        colorForm = ColorForm(instance=color)
    return render(request, 'management/color_details.html', context={'color': color, 'colorForm': colorForm})
