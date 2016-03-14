
from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from .models import newpost

# Create your views here.



#  View for  Home page

def post_list(request):

    posts = newpost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request , 'myblog/post_list.html', {'posts':posts  })


#   View for A Particular post

def post_page(request , post_id):

    post = get_object_or_404(newpost , pk=post_id);

    return render(request, 'myblog/post_page.html' , { 'post' : post } );
