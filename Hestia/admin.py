# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User
from .models import Video
from .models import Condition
from .models import Question
from .models import Answer

admin.site.register(User)
admin.site.register(Video)
admin.site.register(Condition)
admin.site.register(Question)
admin.site.register(Answer)