from django.contrib.auth import get_user_model
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()
user_model = get_user_model()

@register.filter
def author_details(author, curr_user):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"
    
    if author.email == curr_user.email:
        return format_html("<strong>me</strong>")

    if author.email:
        email = author.email
        prefix = f'<a href="mailto:{email}">'
        suffix = "</a>"
    else:
        prefix = ""
        suffix = ""

    return format_html("{}{}{}", prefix, name, suffix)