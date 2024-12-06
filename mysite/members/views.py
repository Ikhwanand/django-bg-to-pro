from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Member

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    firstnames = Member.objects.values_list('firstname')
    return render(request, 'all_members.html', {'mymembers': mymembers, 'firstnames': firstnames})


def details(request, slug):
    mymember = get_object_or_404(Member, slug=slug)
    return render(request, 'details.html', {'mymember': mymember})

def main(request):
    return render(request, 'main.html')

def testing(request):
    mymembers = Member.objects.all().values()
    fruits=["Banana", "Orange", "Lemon", "Papaya"]
    return render(request, 'template.html', {'mymembers': mymembers, 'fruits': fruits})