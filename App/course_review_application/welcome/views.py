from django.shortcuts import render
import welcome.views
# Create your views here.
def welcome_view(request):
    return render(request, 'index.html', {})