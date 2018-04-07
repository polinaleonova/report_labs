import datetime
from django import template

register = template.Library()

@register.simple_tag()
def date_formatting(date_string, curr_format, req_format):
    """

    :param date_string: string with date like "2017-01-05 Thursday"
    :param curr_format: string with current formatting of date_string, like '%Y-%m-%d %A'
    :param req_format: string with result formatting of date
    :return: string in required format
    """
    current_datetime = datetime.datetime.strptime(date_string, curr_format)
    result_datetime = current_datetime.strftime(req_format)
    return result_datetime