from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from .models import UserMtAccounts
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, AccountUpdateForm, UserRegistrationForm, UserMtAccountsCreation, InputForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
import locale
from decouple import config
from django.http import JsonResponse
import asyncio
from metaapi_cloud_sdk import MetaApi
from metaapi_cloud_sdk.clients.metaApi.tradeException import TradeException
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from asgiref.sync import sync_to_async

myAccount = ""

token = config('token')
api = MetaApi(token=token)


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'users/password_success.html', {})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'register'})


@login_required
def account(request):
    # account create form
    mt_account_id = ""
    account_created = False
    requested_accounts = UserMtAccounts.objects.filter(user=request.user).order_by('-date_created')
    input_form = InputForm()

    if request.method == "POST":
        form = UserMtAccountsCreation(request.POST)
        input_form = InputForm(request.POST)
        if form.is_valid() and input_form.is_valid():
            account_name = form.cleaned_data.get('account_name')
            account_login = input_form.cleaned_data.get('account_login')
            account_password = input_form.cleaned_data.get('account_password')
            server_name = input_form.cleaned_data.get('server_name')

            # check if account name already exist,if it does this function should not run
            if not UserMtAccounts.objects.filter(account_name=account_name).exists():
                account_mt = asyncio.run(create_account(account_name, account_login, account_password, server_name))
                mt_account_id = account_mt.id
                UserMtAccounts.objects.create(user=request.user, account_name=account_name, account_id=mt_account_id)
    else:
        form = UserMtAccountsCreation()
        # input_form = InputForm()

    # profile update form
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = AccountUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Changes made successfully")
            return redirect('account')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = AccountUpdateForm(instance=request.user.profile)

    context = {

        "form": form,
        "input_form": input_form,
        "requested_accounts": requested_accounts,
        'u_form': u_form,
        'p_form': p_form
    }

    if request.is_ajax():
        mt_account = render_to_string("users/account_form.html", context, request=request)
        return JsonResponse({
            "form": mt_account
        })

    return render(request, 'users/account.html', context)


async def create_account(a_name, a_login, a_password, a_server):
    accounts = await api.metatrader_account_api.create_account(account={
        'name': a_name,
        'type': 'cloud',
        'login': a_login,
        # password can be investor password for read-only access
        'password': a_password,
        'server': a_server,
        'provisioningProfileId': "4f807ef0-2978-4a0e-b00f-9003b501e15a",
        'application': 'MetaApi',
        'magic': 123456,
        'quoteStreamingIntervalInSeconds': 2.5,  # set to 0 to receive quote per tick
        'reliability': 'regular'

    })
    return accounts


async def remove_account(ac_id):
    user_mt_account = await api.metatrader_account_api.get_account(account_id=ac_id)
    await user_mt_account.remove()


@login_required()
def remove_mt_account(request, id):
    mt_account = get_object_or_404(UserMtAccounts, id=id)
    asyncio.run(remove_account(mt_account.account_id))
    mt_account.delete()

    context = {
        "mt_account": mt_account
    }

    if request.is_ajax():
        u_account = render_to_string("users/remove_account.html", context, request=request)
        return JsonResponse({
            "uaccount": u_account
        })
