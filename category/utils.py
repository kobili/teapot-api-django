from .models import Category
from .exceptions import CategoryNotFoundException

def get_category_by_id(category_id: str):
    category = Category.objects.filter(category_id=category_id).first()
    if not category:
        raise CategoryNotFoundException(category_id)
    
    return category
