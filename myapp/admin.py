from django.contrib import admin
from myapp.models import Record, Customer


class RecordAdmin(admin.ModelAdmin):
  list_display = ("phone_number", )


class CustomerAdmin(admin.ModelAdmin):
  list_display = ("phone_number", "customer_name")


admin.site.register(Record, RecordAdmin)
admin.site.register(Customer, CustomerAdmin)
