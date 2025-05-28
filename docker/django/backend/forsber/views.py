from django.shortcuts import render

# Create your views here.
def photo_view(request):
    return render(request, 'photo_page.html')