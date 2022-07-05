from django.shortcuts import render


def index(request):
    return render(request, 'monarp_site/index.html')

def signup(request):
    return render(request, 'monarp_site/signup.html')
