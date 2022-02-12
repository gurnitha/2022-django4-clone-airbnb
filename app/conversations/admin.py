# app/conversatons/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.conversations.models import Conversation, Message

# Register your models here.

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
	pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	pass
