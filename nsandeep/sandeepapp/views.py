from django.shortcuts import render
from .models import Banner,Portfolio,About,BrandSlider,OurClientReview,BlogPost,Contact
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
# Create your views here.
def home(request):
    banner_item = Banner.objects.last()
    about_item = About.objects.last()
    portitem_item = Portfolio.objects.all()
    brand_logo = BrandSlider.objects.last()
    ourClients = OurClientReview.objects.all()
    # post = BlogPost.objects.all()
    
    object_list = BlogPost.objects.filter(status=1).order_by('Create_at')
    paginator = Paginator(object_list, 3) 

    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post = paginator.page(paginator.num_pages)
    

    #Contact 
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        message = request.POST.get('message',"")
        
        oContactinfo = Contact(Name=name,Email=email,Message=message)
        oContactinfo.save()
    
        sucess =f'hi {name} sucessfully Sending email'
        subject = ''
        message ='''
        Subject:{}
        Message:{}
        From:{}
        '''.format(subject,message,email)
        try:
            send_mail(subject, message,'noreplayitsnsandeep@gmail.com',recipient_list=['admin@itsnsandeep.com']) 
            messages.success(request,sucess)
        except:
            messages.error(request,'your emails sending fail')

    return render(request, 'uifiles/index.html', {'banner_item':banner_item,'portitem_item':portitem_item,'about_item':about_item,'brand_logo':brand_logo,'ourClients':ourClients,'post':post ,'page': page})


def Post_Item(request, id):
    selectpost = BlogPost.objects.get(Id=id)
    return render(request, 'uifiles/blog-single.html',{'selectpost':selectpost})



def page_not_found_view(request, exception):
    return render(request, 'uifiles/404.html', status=404)