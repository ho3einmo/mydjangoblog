from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is the about page.")
    

# The above code is a Django view function that handles requests to the "about" page.
def home(request):
    return HttpResponse("This is the home page.")