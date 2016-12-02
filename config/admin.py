from django.contrib import admin
from models import Config

class ConfigAdmin(admin.ModelAdmin):
    fields = ('device_id', 'cool_down', 'max_sessions', 'native_theme',
              'rescue_video', 'lose_video', 'win_video', 'preroll_video',
              'app_startup_video', 'sponsored_enable', 'sponsored_frequency',
              'location_wallpaper', 'reset'
    )

admin.site.register(Config, ConfigAdmin)
