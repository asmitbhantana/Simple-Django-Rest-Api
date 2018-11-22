from django.contrib import admin
from .models import *


class ClubAdmin(admin.ModelAdmin):
    list_display = ['clubName', 'clubDescription']
    


admin.site.register(Club, ClubAdmin)

class clubImagesUrlAdmin(admin.ModelAdmin):
    list_display = ['club']



admin.site.register(clubImagesUrl, clubImagesUrlAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ['memberName', 'memberPosition', 'club']


admin.site.register(Member, MemberAdmin)

class ClubNoticeAdmin(admin.ModelAdmin):
    list_display = ['noticeTitle', 'club', 'eventDescription', 'eventDate']
    list_filter = ['eventDate']


admin.site.register(ClubNotice, ClubNoticeAdmin)
# Register your models here.
