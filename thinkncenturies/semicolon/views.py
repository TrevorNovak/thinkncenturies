from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'semicolon/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts. """
        return Post.objects.order_by('-created_on')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'semicolon/detail.html'
