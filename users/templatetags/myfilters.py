from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.simple_tag
def keyvalue(list, key, total):
    for item in list:
        if item['value'] == int(key):
            return round(item['total']/total*100, 2)
    return 0
