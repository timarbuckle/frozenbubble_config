from django.http import JsonResponse
from config.models import Config


def appconfig(request, device_id):
    try:
        config = Config.objects.get(device_id=device_id)
    except Config.DoesNotExist:
        config = Config.objects.create(device_id=device_id)
    data = {
        "device_id": config.device_id,
        "cool_down": {
            "enable": config.cool_down,
            "max_sessions": config.max_sessions
        },
        "native_theme": config.native_theme,
        "rewarded_video": {
            "rescue_video": config.rescue_video,
            "lose_video": config.lose_video,
            "win_video": config.win_video,
            "preroll_video": config.preroll_video,
            "app_startup_video": config.app_startup_video
        },
        "sponsored_product": {
            "enable": config.sponsored_enable,
            "frequency": config.sponsored_frequency
        },
        "location_wallpaper": config.location_wallpaper,
        "reset": config.reset
    }
    # only use the reset once per setting
    if config.reset:
        config.reset = False
        config.save()

    return JsonResponse(data)
