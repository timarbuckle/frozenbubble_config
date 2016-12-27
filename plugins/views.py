import os
import hashlib

from django.http import HttpResponse
from django.conf import settings

VALID_PLUGIN_NAMES = ['adview']


def get_plugin(request, plugin_name, checksum=None):
    response = None
    if plugin_name in VALID_PLUGIN_NAMES:
        response = _get_plugin_response(request, plugin_name, checksum)
    else:
        response = HttpResponse()
        response.status_code = 404

    return response


def _get_plugin_response(request, plugin_name, checksum=None):
    plugin_filename = plugin_name + '_plugin.apk'
    plugin_filepath = os.path.join(settings.STATIC_ROOT, plugin_filename)

    if (checksum is not None and
            checksum == _get_checksum(plugin_filepath)):
        response = HttpResponse()
        response.status_code = 204
        return response

    with open(plugin_filepath) as plugin_file:
        response = HttpResponse(content=plugin_file)
        response['Content-Type'] = 'application/vnd.android.package-archive'
        response['Content-Disposition'] = \
            'attachment; filename="' + plugin_filename + '"'
        return response


def _get_checksum(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()
