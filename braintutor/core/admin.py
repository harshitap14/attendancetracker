from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(LearningProfile)
admin.site.register(Avatar)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(UserLesson)
admin.site.register(ProgressReport)
admin.site.register(EmotionTracking)
admin.site.register(Achievement)
admin.site.register(AccessibilitySetting)
