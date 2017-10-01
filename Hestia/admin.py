# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Parent
from .models import Video
from .models import Condition

admin.site.register(Parent)
admin.site.register(Video)
admin.site.register(Condition)