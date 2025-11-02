from django.contrib import admin
from .models import Bus,Driver,DrowsinessEvent
# Register your models here.
admin.site.register(Bus)
admin.site.register(DrowsinessEvent)
admin.site.register(Driver)

