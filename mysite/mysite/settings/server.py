from base import *



DEBUG=False

#when diploy nginx server , we need collect all django's static files
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_ROOT='/root/my_website_server/upload_assets'

IMAGE_CACHE_ROOT='/root/my_website_server/upload_assets'