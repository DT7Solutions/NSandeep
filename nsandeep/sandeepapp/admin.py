from django.contrib import admin
from .models import Banner,About,Portfolio,BrandSlider,OurClientReview,Category,BlogPost,Contact

# Register your models here.


# Register your models here.
class AdminBanner(admin.ModelAdmin):
    list_display=('Id','Title','Description' ,'Image')

class AdminPortfolio(admin.ModelAdmin):
    list_display=('Id','Title','Description' ,'Image')

class AdminAbout(admin.ModelAdmin):
    list_display=('Id','Title','Description' ,'Image')

class AdminBrandSlider(admin.ModelAdmin):
    list_display=('Id','Image')

class AdminHappyClients(admin.ModelAdmin):
    list_display=('Id','Name','Message','Image')

class AdminHappyCategories(admin.ModelAdmin):
    list_display=('Name','Created')

class AdminHappyBlogpost(admin.ModelAdmin):
    list_display=('Id','Category','Title','Tags','CreatedName','Create_at','status')
    list_filter = ["CreatedName",'Create_at']

class AdminContact(admin.ModelAdmin):
    list_display=('Id','Name','Email' ,'Message')

admin.site.register(Banner,AdminBanner)
admin.site.register(About,AdminAbout)
admin.site.register(Portfolio,AdminPortfolio)
admin.site.register(BrandSlider,AdminBrandSlider)
admin.site.register(OurClientReview,AdminHappyClients)

admin.site.register(Category,AdminHappyCategories)
admin.site.register(BlogPost,AdminHappyBlogpost)

admin.site.register(Contact,AdminContact)