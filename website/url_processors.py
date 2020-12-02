from .models import Category

def PageMeta(request):
    cat_url = Category.objects.values_list('name', 'slug')
    return {
        'cat_url': cat_url,  # Add 'contacts' to the context
    }