from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_size_kb = 50

    if max_size_kb*1024 < file.size:
        raise ValidationError(
            f'file can not be loaded max size: {max_size_kb}')
