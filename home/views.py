from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, BlogComments
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'blog.html', context)

def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComments.objects.all().filter(post=post)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'post.html', context)

def signupUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        users = User.objects.create_user(username, email, pass1)
        users.first_name = fname
        users.last_name = lname
        users.save()
        user = authenticate(username=username, password=pass1)
        login(request, user)
        return redirect('blog')
    return render(request, 'signup.html')

def loginUser(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)
        login(request, user)
        return redirect('blog')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('blog')

def uploadPost(request):
    if request.method == 'POST' and request.FILES : 
        title = request.POST['title']
        category = request.POST['category']
        slug = request.POST['slug']
        author = request.user
        uploadImg = request.FILES['uploadImg']
        content = request.POST['content']

        UploadPosts = Post(title=title, category=category, slug=slug, image=uploadImg, content=content, author=author)
        UploadPosts.save()
        return redirect('blog')
    return render(request, 'upload.html')

def postComments(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)

        comments = BlogComments(comment=comment, user=user, post=post)
        comments.save()
    return redirect(f'/{post.slug}')

def search(request):
    query = request.GET['query']
    allPostsTitle = Post.objects.filter(title__icontains=query)
    allPostsContent = Post.objects.filter(content__icontains=query)
    allPosts = allPostsTitle.union(allPostsContent)

    params = {
        'allPosts': allPosts
    }
    return render(request, 'search.html', params)