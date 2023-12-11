from django.contrib import admin

# Register your models here.
from .models import Form
from .models import Feedback
from .models import Cod

  

# Register your models here.
admin.site.register(Form)
admin.site.register(Feedback)
admin.site.register(Cod)

