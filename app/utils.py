from conf.settings import ALLOWED_IMAGE_TYPE


def allowed_image(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_TYPE
