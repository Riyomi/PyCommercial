from django import template
from math import floor, ceil


register = template.Library()


@register.filter(name='formaturl')
def format_url(url):
    stripped = url.split('/')[2:]
    return '/' + '/'.join(stripped)


@register.filter(name='truncatetext')
def truncate_text(text, param):
    return (text[:param] + '..') if len(text) > param else text


@register.filter(name='encoderating')
def encode_rating(rating):

    if rating is None:
        return [0] * 5

    encoded = []
    rating_rounded = round(float(rating) * 2) / 2.0

    encoded.extend([1] * (floor(rating_rounded)))
    # checks if the rounded rating has 0.5. It's done this way to avoid rounding errors
    if (rating_rounded - 0.5) % 1 == 0:
        encoded.append(0.5)
    encoded.extend([0] * ((5-(ceil(rating_rounded)))))

    return encoded


@register.filter
def encode_url(value):
    return value.replace(' ', '+').replace('&', '%26')


@register.simple_tag
def keyvalue(list, key, total):
    for item in list:
        if item['value'] == int(key):
            return round(item['total']/total*100, 2)
    return 0
