from django import template

register = template.Library()

@register.filter(name='time_difference')
def time_difference(submit_time, end_time):
    # Calculate the difference
    diff = submit_time - end_time
    # Convert the difference to minutes
    return diff.total_seconds() / 60  # Returns the difference in minutes

@register.filter(name='to_int')
def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return value 