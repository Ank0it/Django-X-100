from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello, you are about to witness genius")
    return render(request,'website/index.html')

    
def about(request):
    return HttpResponse("hello, you are about to know about")
    

def contact(request):
    return HttpResponse("hello, you should not contact ever")