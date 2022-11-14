
from django.contrib import admin

from home.models import Contact, Event, Gallery, PostBearer, Announcement, carousel, Post, StudentChapter, FacultyChapter

# Register your models here.

admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(PostBearer)
admin.site.register(Event)
admin.site.register(Announcement)
admin.site.register(Gallery)
admin.site.register(carousel)
admin.site.register(StudentChapter)
admin.site.register(FacultyChapter)