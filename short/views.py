from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from .models import SHORTURL
from .forms import SHORTURLForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import DetailView, ListView
# Create your views here.

def urliew(request, id):
    url_shortened = get_object_or_404(SHORTURL, id=id)
    return redirect(url_shortened.orignalurl)

class ShortenedUrlView(CreateView):
    form_class = SHORTURLForm
    template_name = "home.html"
    success_url = reverse_lazy("main")
    def get_context_data(self, **kwargs):
        self.shortened_urls = SHORTURL.objects.all()
        kwargs['shortened_urls'] = self.shortened_urls
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        form.instance.url_path = self.request.build_absolute_uri(form.instance.get_absolute_url())
        return super().form_valid(form)

def works(request):
    template_name = "short/works.html"
    return render(request, template_name, {})