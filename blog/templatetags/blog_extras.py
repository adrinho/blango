from django import template
from django.contrib.auth.models import User
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def author_details(author, current_user=None):
    if not isinstance(author, User):
        return ''
    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{escape(author.first_name)} {escape(author.last_name)}"
    else:
        name = escape(author.username)
    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")

    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)
