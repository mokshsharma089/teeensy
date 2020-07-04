from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from shortner.models import rickUrl
from django.views import View
from shortner.forms import SubmitUrlForm
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "RickUrl.co",
            "form": the_form
        }
        return render(request, "home/home.html", context) 

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            if "http://" not in new_url and "https://" not in new_url:
                new_url="http://"+new_url
            obj, created = rickUrl.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
                "form": form
            }
        if created:
                template = "home/sucess.html"
        else:
                template = "home/failure.html"
    
        return render(request, template ,context)

def view1(request,slug,*args,**kwargs):
    shortname=slug
    obj=get_object_or_404(rickUrl,shortcode=shortname)
    return HttpResponseRedirect(obj.url)
    