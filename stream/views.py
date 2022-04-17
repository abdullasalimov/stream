from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def blog_index(request):
    return render(request, 'blog/index.html')

def blog_post(request):
    return render(request, 'blog/post.html')

def news_index(request):
    return render(request, 'news/index.html')

def news_single(request):
    return render(request, 'news/single-page.html')

def speaking(request):
    return render(request, 'speaking/upload.html')

def listening_single(request):
    return render(request, 'listening/single-channel.html')

def listening_video(request):
    return render(request, 'listening/video-page.html')

def writing_index(request):
    return render(request, 'writing/index.html')

def writing_newpost(request):
    return render(request, 'writing/newpost.html')

def writing_post(request):
    return render(request, 'writing/post.html')

def reading_index(request):
    return render(request, 'reading/index.html')

def reading_detail(request):
    return render(request, 'reading/detail.html')

def reading_listing(request):
    return render(request, 'reading/listing.html')