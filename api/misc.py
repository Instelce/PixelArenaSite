import os


def get_upload_path(instance, filename):
    """ creates unique-Path & filename for upload """

    return os.path.join(
        'graphics/', instance.item.category.name, instance.item.name, filename
    )