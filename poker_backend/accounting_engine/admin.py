from django.contrib import admin
from accounting_engine.models import AccountReport, AgentReport
# Register your models here.
admin.site.register(AccountReport)
admin.site.register(AgentReport)
