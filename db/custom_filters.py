from django import template

register = template.Library()


@register.filter
def isinstance(value, class_str):
    try:
        class_obj = eval(class_str)
        return isinstance(value, class_obj)
    except (NameError, TypeError):
        return False