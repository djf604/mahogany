__author__ = 'Dominic Fitzgerald'
from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import Page, RichTextPage
from models import HomePage, Event


class HomePageAdmin(PageAdmin):
    pass

# admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Event)


from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost

page_fieldsets = deepcopy(PageAdmin.fieldsets)
page_fieldsets[0][1]['fields'].insert(2, u'background')
# page_fieldsets[0][1]['fields'] += ('background',)
PageAdmin.fieldsets = page_fieldsets

print page_fieldsets

# class MyPageAdmin(PageAdmin):
    # fieldsets = page_fieldsets

# print MyPageAdmin.fieldsets

# admin.site.unregister(HomePage)
admin.site.unregister(RichTextPage)
admin.site.unregister(Page)
admin.site.register(RichTextPage, PageAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(HomePage, PageAdmin)
