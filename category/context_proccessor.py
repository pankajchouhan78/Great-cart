from .models import Category

def mainu_links(request):
    links = Category.objects.all()
    return dict(links = links)