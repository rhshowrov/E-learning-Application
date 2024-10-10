from django import template
from urllib.parse import urlparse, parse_qs

register = template.Library()

@register.filter(name='range_filter')
def range_filter(value):
  return value[:53]+'....'