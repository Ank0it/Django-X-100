from .models import AppVariety
from django.shortcuts import get_object_or_404, render
# Create your views here.
def all_app(request):
    apps = AppVariety.objects.all()
    return render(request,'app/all_app.html',{'apps': apps})

def app_details(request,app_id):
    app = get_object_or_404(AppVariety, pk=app_id)
    return render(request,'app/app_details.html',{'app':app })     