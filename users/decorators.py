from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            
            user_groups = request.user.groups.all()
            user_groups_names = []
            
            for item in user_groups:
                user_groups_names.append(item.name)
            
            
            if set(user_groups_names) & set(allowed_roles):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden()
            
        return wrapper
    
    return decorator