from django.contrib.auth.models import AbstractUser
from django.db import models

# --------------------
# CUSTOM USER MODEL
# --------------------
class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('parent', 'Parent'),
        ('educator', 'Educator'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    age = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=20, null=True, blank=True)

# --------------------
# LEARNING PROFILE (Dynamic based on user type)
# --------------------
class LearningProfile(models.Model):
    LEARNING_STYLE_CHOICES = [
        ('visual', 'Visual'),
        ('auditory', 'Auditory'),
        ('kinesthetic', 'Kinesthetic'),
        ('mixed', 'Mixed'),
        ('routine','routine')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Common fields for all users
    pace = models.CharField(max_length=20, default='moderate')
    subject_interests = models.JSONField(default=list)  # Example: ["Math", "Science"]
    session_time_limit = models.PositiveIntegerField(default=15)  # In minutes
    reward_system_enabled = models.BooleanField(default=True)

    # Neurodivergent flag
    neurodivergent_support_enabled = models.BooleanField(default=False)

    # Optional fields — used only if neurodivergent support is ON
    learning_style = models.CharField(
        max_length=20,
        choices=LEARNING_STYLE_CHOICES,
        null=True,
        blank=True
    )
    calm_mode = models.BooleanField(default=False)
    background_light_setting = models.CharField(
        max_length=20,
        choices=[('soft', 'Soft'), ('dark', 'Dark'), ('neutral', 'Neutral')],
        default='neutral',
        null=True,
        blank=True
    )
    text_to_speech = models.BooleanField(default=False)
    activity_based_learning = models.BooleanField(default=False)
    sound_flexibility = models.BooleanField(default=False)
    quiz_mode_enabled = models.BooleanField(default=False)

# --------------------
# AVATAR CUSTOMIZATION
# --------------------
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appearance = models.CharField(max_length=100)
    voice_tone = models.CharField(max_length=50, default='neutral')
    voice_speed = models.CharField(max_length=20, default='normal')
    empathy_level = models.CharField(max_length=20, default='medium')

# --------------------
# SUBJECT & LESSONS
# --------------------
class Subject(models.Model):
    name = models.CharField(max_length=50)
    level_range = models.CharField(max_length=50)

class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=20)
    content_json = models.JSONField()  # Structured lesson content
    visual_assets = models.JSONField(default=dict)  # Example: {"image": "fractions_pizza.png"}

# --------------------
# USER'S LEARNING TRACKING
# --------------------
class UserLesson(models.Model):
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    score = models.IntegerField(null=True, blank=True)
    
    # Optional for mood-based feedback (for neurodivergent users)
    mood_check = models.CharField(max_length=10, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

# --------------------
# LEARNING REPORT
# --------------------
class ProgressReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_spent = models.IntegerField()  # In minutes
    correct_answers = models.IntegerField()
    mood_trend = models.TextField(blank=True)
    recommendations = models.TextField()

# --------------------
# EMOTION ANALYSIS (only used if neurodivergent_support_enabled is True)
# --------------------
class EmotionTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    facial_emotion = models.CharField(max_length=50, null=True, blank=True)
    voice_sentiment = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

# --------------------
# BADGES AND REWARDS
# --------------------
class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge_name = models.CharField(max_length=100)
    date_awarded = models.DateTimeField(auto_now_add=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True)

# --------------------
# OPTIONAL ACCESSIBILITY SETTINGS
# --------------------
class AccessibilitySetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sensory_controls = models.JSONField(default=dict)  # e.g. {"animation_speed": "slow"}
    communication_mode = models.CharField(max_length=20, default='text_voice')  # text / voice / hybrid
    interface_preferences = models.JSONField(default=dict)  # font size, UI adjustments
    permissions = models.JSONField(default=dict)  # e.g., {"emotion_tracking": true}
