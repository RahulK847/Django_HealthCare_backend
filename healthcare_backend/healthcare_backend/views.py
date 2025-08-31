from django.shortcuts import render
from django.http import HttpResponse

def api_documentation(request):

    return render(request, 'api_docs.html')

def health_check(request):
    return HttpResponse("Healthcare Backend API is running! 🏥", content_type="text/plain")
