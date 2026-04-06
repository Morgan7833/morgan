from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import Message


User = get_user_model()


@login_required
def message_list(request):
    messages_qs = Message.objects.filter(receiver=request.user)[:50]
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'messages/list.html', {"messages": messages_qs, "users": users})


@login_required
def send_message(request):
    if request.method == 'POST':
        to_id = request.POST.get('to')
        subject = request.POST.get('subject', '')
        body = request.POST.get('body', '')
        if to_id and body:
            receiver = User.objects.get(pk=to_id)
            Message.objects.create(sender=request.user, receiver=receiver, subject=subject, body=body)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"ok": True})
            return redirect('messages:list')
    return JsonResponse({"ok": False}, status=400)


@login_required
def poll_messages(request):
    last_id = request.GET.get('last_id')
    qs = Message.objects.filter(receiver=request.user)
    if last_id:
        qs = qs.filter(id__gt=last_id)
    data = [
        {"id": m.id, "from": m.sender.get_full_name() or m.sender.username, "subject": m.subject, "body": m.body, "ts": m.timestamp.isoformat()}
        for m in qs.order_by('-id')[:50]
    ]
    return JsonResponse({"messages": data})

# Create your views here.
