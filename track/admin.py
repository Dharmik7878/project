from django.contrib import admin
from track.models import *

class ProductDetailAdmin(admin.ModelAdmin):
    list_display=('id','productname','tracknumber','status','origin','destination','estimatedlv','dateshiped')

admin.site.register(ProductDetail,ProductDetailAdmin)