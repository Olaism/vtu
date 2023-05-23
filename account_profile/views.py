from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProfileEditForm
from .models import Profile


@login_required
def profile(request):
    return render(request, "account/profile.html")


@login_required
def profile_update(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.save()
            profile = form.save()
            return redirect("profile:index")

    else:
        form = ProfileEditForm()
    return render(request, "account/profile_update.html", {"form": form})
