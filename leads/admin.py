from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("email", "source", "contacted", "created_at")
    list_filter = ("contacted", "source")
    search_fields = ("email",)
    ordering = ("created_at",)
