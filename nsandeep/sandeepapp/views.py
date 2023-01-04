from django.shortcuts import render

# Create your views here.
# Create your views here.
def home(request):
    return render(request, 'uifiles/index.html')


def page_not_found_view(request, exception):
    return render(request, 'uifiles/404.html', status=404)