from django.contrib import admin

from .models import Page, PagePassword, VisiblePage, CurrentGame

class PagePasswordInline(admin.TabularInline):
    model = PagePassword
    fk_name = 'page'
    extra = 1

class PagePasswordAdmin(admin.ModelAdmin):
    pass

class PageAdmin(admin.ModelAdmin):
    inlines = [ PagePasswordInline ]

class VisiblePageAdmin(admin.ModelAdmin):
    pass

class CurrentGameAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)
admin.site.register(PagePassword, PagePasswordAdmin)
admin.site.register(VisiblePage, VisiblePageAdmin)
admin.site.register(CurrentGame, CurrentGameAdmin)
