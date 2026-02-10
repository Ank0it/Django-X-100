from django.contrib import admin 
from .models import AppVariety, AppReviews, Store, AppCertificate 

# Register your models here. 
class AppReviewInline(admin.TabularInline):
    model = AppReviews
    extra =2
class AppVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type','date_added')
    inlines = [AppReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('app_varieties',) 

class AppCertificateAdmin(admin.ModelAdmin):
    list_display = ('app', 'certificate_number')             

admin.site.register(AppVariety, AppVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(AppCertificate, AppCertificateAdmin)