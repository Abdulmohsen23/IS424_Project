from django.shortcuts import redirect
from django.urls import reverse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.path != reverse('log_in') and request.path != reverse('register'):
                return redirect(reverse('log_in'))

        response = self.get_response(request)
        return response
