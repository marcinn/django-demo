from demoapp.forms import DemoLoginForm
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from demoapp import app_settings
from demoapp.utils import get_salt


def login_view(request):
    if request.method == 'POST':
        form = DemoLoginForm(request.POST)
        if form.is_valid():
            response = redirect('/')
            response.set_signed_cookie(app_settings.COOKIE_NAME, 'demo access granted', salt=get_salt(request))
            return response
    else:
        form = DemoLoginForm()
    return render_to_response('demoapp/login.html', {'form': form})
