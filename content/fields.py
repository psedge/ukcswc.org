import sys
from io import BytesIO

from django import forms
from django.core.exceptions import ValidationError
from django.utils import six


class MultipleImageField(forms.fields.FileField):
    default_error_messages = {
        'invalid_image': (
            "Upload a valid image. The file you uploaded was either not an "
            "image or a corrupted image."
        ),
    }

    def to_python(self, data):
        """
        Checks that the file-upload field data contains a valid image (GIF, JPG,
        PNG, possibly others -- whatever the Python Imaging Library supports).
        """
        f = super(MultipleImageField, self).to_python(data)
        if f is None:
            return None

        from PIL import Image

        # We need to get a file object for Pillow. We might have a path or we might
        # have to read the data into memory.
        if hasattr(data, 'temporary_file_path'):
            file = data.temporary_file_path()
        else:
            if hasattr(data, 'read'):
                file = BytesIO(data.read())
            else:
                file = BytesIO(data['content'])

        try:
            # load() could spot a truncated JPEG, but it loads the entire
            # image in memory, which is a DoS vector. See #3848 and #18520.
            image = Image.open(file)
            # verify() must be called immediately after the constructor.
            image.verify()

            # Annotating so subclasses can reuse it for their own validation
            f.image = image
            # Pillow doesn't detect the MIME type of all formats. In those
            # cases, content_type will be None.
            f.content_type = Image.MIME.get(image.format)
        except Exception:
            # Pillow doesn't recognize it as an image.
            six.reraise(ValidationError, ValidationError(
                self.error_messages['invalid_image'],
                code='invalid_image',
            ), sys.exc_info()[2])
        if hasattr(f, 'seek') and callable(f.seek):
            f.seek(0)
        return f

