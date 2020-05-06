from django.contrib import admin
from agents.models import Club, Agent, Account
# Register your models here.

"""
class AccountInline(admin.StackedInline):
    model = Account.agent.through
    extra = 1


class AgentAdmin(admin.ModelAdmin):
    inlines = [AccountInline]


class AccountAdmin(admin.ModelAdmin):
    filter_horizontal = ("agent",)
"""

admin.site.register(Club)
admin.site.register(Agent)
admin.site.register(Account)
