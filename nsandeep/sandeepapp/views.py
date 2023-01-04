from django.shortcuts import render
from .models import Banner,Portfolio,About,BrandSlider,OurClientReview,BlogPost
# Create your views here.
# Create your views here.
def home(request):
    banner_item = Banner.objects.all()
    about_item = About.objects.all()
    portitem_item = Portfolio.objects.all()
    brand_logo = BrandSlider.objects.all()
    ourClients = OurClientReview.objects.all()
    post = BlogPost.objects.all()
    return render(request, 'uifiles/index.html', {'banner_item':banner_item,'portitem_item':portitem_item,'about_item':about_item,'brand_logo':brand_logo,'ourClients':ourClients,'post':post})


def Post_Item(request, id):
    print('------------------------------------------------------------------')
    print(id)
    selectpost = BlogPost.objects.get(Id=id)
    print(selectpost.Id)
    return render(request, 'uifiles/blog-single.html',{'selectpost':selectpost})



def page_not_found_view(request, exception):
    return render(request, 'uifiles/404.html', status=404)