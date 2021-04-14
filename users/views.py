from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    """
    Register View.

    Allows the user to get the registration page and create a new account.
    """

    # If the form is submitted
    if request.method == 'POST':

        # Populate the form with the user's details
        form = UserRegisterForm(request.POST)

        # Check if the form is valid
        if form.is_valid():

            # Save the new user in the database
            form.save()

            # Get the user's first name and use it to flash him a success message
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'{first_name}, contul tău a fost creat! Te poți autentifica.')

            # Redirect the user to log into his account
            return redirect('login')

    # If the page method's is GET, load the form
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """
    Profile View.

    Allows user to see the details connected to his account.
    """

    # If the form is submitted
    if request.method == "POST":

        # Populate the form with user's details
        user_update_form = UserUpdateForm(request.POST, instance=request.user)

        # Populate the form with user's profile image
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # If forms are valid, save data
        if user_update_form.is_valid() and profile_form.is_valid():
            user_update_form.save()
            profile_form.save()

            # Flash a success message to the user
            messages.success(request, "Contul tău a fost actualizat!")

            return redirect('profile')

    # If the page method's is GET, populate the forms with user's existing data
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_update_form': user_update_form,
        'profile_form': profile_form,
    }

    return render(request, 'users/profile.html', context=context)
