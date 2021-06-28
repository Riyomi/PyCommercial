from django import template

register = template.Library()


@register.filter(name='formaturl')
def format_url(url):
    stripped = url.split('/')[2:]
    return '/' + '/'.join(stripped)


@register.filter(name='truncatetext')
def truncate_text(text):
    return (text[:100] + '..') if len(text) > 100 else text
