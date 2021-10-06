from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileEditionForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Merci {username}, votre compte a été créé avec succés, vous pouvez maintenant vous connecter'
                )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):

    user_pk = request.user.pk
    user_profile = Profile.objects.get(user_id=user_pk)
    subscriptions = user_profile.interests.all()

    if request.method == "POST":
        edit_form = ProfileEditionForm(request.POST, instance=request.user.profile)

        if edit_form.is_valid():
            try:
                edit_form.save()
                messages.success(request, "Merci, vos preferences ont été mises à jour.")
                return redirect('profile')
            except ValueError:
                messages.error(request, "Action impossible")
                return redirect('profile')
    else:
        edit_form = ProfileEditionForm(instance=request.user.profile)

    context = {
        "title": "Mon Profil",
        "subscriptions": subscriptions,
        "edit_form": edit_form,
    }
    return render(request, 'user/profile.html', context)
