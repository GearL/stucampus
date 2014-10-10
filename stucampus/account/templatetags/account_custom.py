# -*- coding:utf-8
from hashlib import md5

from django import template
from django.contrib.auth.models import User


register = template.Library()


@register.filter(name='user_avatar')
def user_avatar(user):
    if isinstance(user, User):
        email = user.email
        hashed_email = md5(email).hexdigest()
        return hashed_email
    else:
        return None


@register.filter(name='get_college_name')
def get_college_name(student):
    college_id = student.college
    if college_id:
        return student.get_college_display()
    else:
        return '暂无'


@register.filter(name='get_student_status', is_safe=True)
def get_student_status(student):
    is_active = student.user.is_active
    if is_active is False:
        return '禁用'
    else:
        return '正常'
