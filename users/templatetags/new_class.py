from django import template

register = template.Library()

@register.filter(name='new_class')
def new_class(value, arg):
    return value.as_widget(attrs={'class': arg})