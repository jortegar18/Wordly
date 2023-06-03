from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Session)
admin.site.register(Work_Experience)
admin.site.register(Paymenth_Method)
admin.site.register(Tutor)
admin.site.register(Student)