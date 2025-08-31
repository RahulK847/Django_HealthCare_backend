from django.shortcuts import render
from django.http import HttpResponse

def api_documentation(request):
    """
    Serve the API documentation HTML page
    """
    return render(request, 'api_docs.html')

def health_check(request):
    """
    Simple health check endpoint
    """
    return HttpResponse("Healthcare Backend API is running! 🏥", content_type="text/plain")
