from django.http import Http404


def cart_required(the_func):
    def _decorated(request, *args, **kwargs):
        if request.has_cart is False:
            raise Http404
        return the_func(request, *args, **kwargs)
    return _decorated
