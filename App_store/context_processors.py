from .models import Category

def menu(request):
    menu_item = Category.objects.all()
    return dict(menu_item=menu_item)