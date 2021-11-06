from django.forms.models import ModelForm
from django.shortcuts import redirect, render
from .models import Post, Review
from django.views import generic
from .forms import CommentForm
from django.http import Http404

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

def about(request):
    return render(request, 'about.html', {} )
def contact(request):
    return render(request, 'contact.html', {} )

#class DetailView(generic.DetailView):
#    model = Post
#    reviews =
#    template_name = 'post_detail.html'
#class About(generic.DetailView):
#    template_name = 'nav.html'
def project(request , pk):
    #evrey number will take us to his project
    try :
        postobj = Post.objects.get(slug=pk) #get one object only
    except Post.DoesNotExist:
        raise Http404
    #pro = Review.objects.get(slug=pk)
    pro = postobj.review_set.all()
    
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid :
            obj = form.save(commit=False)
            obj.post = postobj
            obj.save()
            return redirect('post_detail',pk=postobj.slug)
    else:
        form = CommentForm

    
    context = {'post':postobj, 'reviews':pro ,'form': form}
    return render(request, 'post_detail.html' , context)
