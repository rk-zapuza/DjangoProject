from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Rohit Kotiyal'
    }
    return render(request, 'index.html', context)


def about(request):
    return  HttpResponse("This is the about page")
