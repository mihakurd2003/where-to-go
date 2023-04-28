from django.utils.html import format_html


class GetPhoto:
    def get_photo(self, image):
        return format_html(
            '<img src="{}" style="max-height: {};"/>',
            image.image.url,
            '200px'
        )
