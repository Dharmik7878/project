from django.contrib import admin
from srvc.models import *

class registerAdmin(admin.ModelAdmin):
    list_display=('rname','runame','remail','rmobile','rcrtpass','rconpass')

class contactAdmin(admin.ModelAdmin):
    list_display=('cname','cemail','csub','cmsg')

class FeedBackAdmin(admin.ModelAdmin):
    list_display=('fbname','fbemail','fbnum','fbsrv','fbmsg')

class ExportFormAdmin(admin.ModelAdmin):
    list_display=('id','CustomerName','Email','contact','Product','Quantity','Country','Shipping','Payment')

class ImportFormAdmin(admin.ModelAdmin):
    list_display=('id','CustomerName','Email','contact','Product','Quantity','St','Shipping','Payment')

admin.site.register(register,registerAdmin)
admin.site.register(contact,contactAdmin)
admin.site.register(FeedBack,FeedBackAdmin)
admin.site.register(ExportForm,ExportFormAdmin)
admin.site.register(ImportForm,ImportFormAdmin)
# Register your models here.