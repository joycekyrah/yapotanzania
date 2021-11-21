from django.shortcuts import render
from core.models import Gallery, Blog, Event, Contact, Leader, Comment, Project, Instagram

def index(request):
    leaders = Leader.objects.all()
    blogs = Blog.objects.all()
    events = Event.objects.all()
    recent_events = Event.objects.all()
    gallerys = Gallery.objects.all()
    projects = Project.objects.all()
    context = {
        'gallerys': gallerys,
        'events': events,
        'recent_events': recent_events,
         'blogs': blogs,
         'leaders': leaders,
         'projects': projects,

    }
    return render(request, 'index.html', context)

def about(request):
    context = {

    }
    return render(request, 'about.html', context)

def events(request):
    events = Event.objects.all()
    context = {
        'events': events

    }
    return render(request, 'events.html', context)

def blog(request):
    blogs = Blog.objects.all()

    context = {
      'blogs': blogs

    }
    return render(request, 'blog.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        user_email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        new_contact = Contact()
        new_contact.name = name
        new_contact.email = user_email
        new_contact.phone = phone
        new_contact.subject = subject
        new_contact.message = message
        new_contact.save()
        
    context = {


    }
    return render(request, 'contact.html', context)

def blog_details(request, blog_id):
    recents = Blog.objects.order_by('-time')[:3]
    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.filter(blog=blog)
    instagram = Instagram.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        user_email = request.POST['email']
        message = request.POST['message']
        new_comment = Comment()
        new_comment.blog = blog
        new_comment.username = name
        new_comment.email = user_email
        new_comment.comment = message
        new_comment.save()
    context = {
        'blog': blog,
        'recents': recents,
        'comments': comments,
       'instagram': instagram,
    
    }
    return render(request, 'blog-details.html', context)

def event_details(request, event_id):
    event = Event.objects.get(id=event_id)

    context = {
        'event': event
    }
    return render(request, 'event-details.html', context)

def gallery(request):
    gallerys = Gallery.objects.all()
    context = {
         'gallerys': gallerys

    }
    return render(request, 'gallery.html', context)


def project(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,

    }
    return render(request, 'donations.html', context)


def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    recents = Blog.objects.order_by('-time')[:3]
    instagram = Instagram.objects.all()
    context = {
       'project': project,
       'recents': recents,
       'instagram': instagram,

    }
    return render(request, 'donation-details.html', context)