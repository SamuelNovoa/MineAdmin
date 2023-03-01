from django import template
from ..forms import CustomAuthenticationForm, CustomCreationForm

register = template.Library()


@register.simple_tag
def login_form():
    return CustomAuthenticationForm(None)


@register.simple_tag
def register_form():
    return CustomCreationForm(None)
