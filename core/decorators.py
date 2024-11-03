from django.shortcuts import redirect


def client_required(view_func):
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'client'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('dashboard')
    return wrapper


def vendor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if hasattr(request.user, 'vendor'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('dashboard')
    return wrapper