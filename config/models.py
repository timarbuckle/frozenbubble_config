from __future__ import unicode_literals

from django.db import models

class Config(models.Model):
    THEMES = (
        ("none", "None"),
        ("starbucks", "Starbucks"),
        ("m&m", "M&M")
    ) 

    device_id = models.CharField(max_length=40)
    cool_down = models.BooleanField(default=False)
    max_sessions = models.PositiveIntegerField(default=2)
    native_theme = models.CharField(max_length=20, choices=THEMES, default="none")
    #rewarded_video = models.BooleanField(default=False)
    rescue_video = models.BooleanField(default=False)
    lose_video = models.BooleanField(default=False)
    win_video = models.BooleanField(default=False)
    preroll_video = models.BooleanField(default=False)
    resume_game_video = models.BooleanField(default=False)
    app_startup_video = models.BooleanField(default=False)
    sponsored_enable = models.BooleanField(default=False)
    sponsored_frequency = models.PositiveIntegerField(default=1)
    location_wallpaper = models.BooleanField(default=False)

    def __unicode__(self):
        return self.device_id
