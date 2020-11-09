from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Site, SiteCategory, SiteSeries
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def single_slug(request, single_slug):
    categories = [c.category_slug for c in SiteCategory.objects.all()]
    if single_slug in categories:
        matching_series = SiteSeries.objects.filter(site_category__category_slug=single_slug)

        series_urls = {}
        for m in matching_series.all():
            part_one = Site.objects.filter(site_series__site_series=m.site_series).earliest("site_published")
            series_urls[m] = part_one.site_slug    

        return render(request,
                      "main/category.html",
                      {"part_ones": series_urls})    
  
    sites = [s.site_slug for s in Site.objects.all()]
    if single_slug in sites:
        this_site = Site.objects.get(site_slug=single_slug)
        sites_from_series = Site.objects.filter(site_series__site_series=this_site.site_series).order_by('site_published')
        this_site_idx = list(sites_from_series).index(this_site)
        
        return render(request=request,
                      template_name='main/site.html',
                      context={"site": this_site,
                               "sidebar": sites_from_series,
                               "this_sit_idx": this_site_idx})

def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories": SiteCategory.objects.all})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
             user = form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f"New Account Created: {username}")
             login(request, user) 
             return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/Register.html",
                          context={"form":form})     
     
    form = UserCreationForm
    return render(request,
                 "main/Register.html",
                 context={"form":form}) 

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})                          
