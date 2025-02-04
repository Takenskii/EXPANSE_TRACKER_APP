from django.contrib import admin
from tracker.models import *
# Register your models here.

admin.site.site_header = "Expanse tracker"
admin.site.site_title = "Expense tracker"

admin.site.register(CurrentBalance)


@admin.action(description="Mark selected stories as Credit")
def make_published(modeladmin, request, queryset):
    queryset.update(status="p")


class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "current_balance",
        "amount",
        "expense_type", 
        "description", 
        "created_at",
    ]

    search_fields = ['expense_type', 'description']
    list_filter = ['expense_type']

admin.site.register(TrackingHistory, TrackingHistoryAdmin)
