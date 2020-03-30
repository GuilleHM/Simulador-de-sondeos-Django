from django.shortcuts import render

# Landing Page
def index(request):
    return render(request, "pages/index.html")
