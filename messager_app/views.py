from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Messages
import json

@method_decorator(csrf_exempt, name='dispatch')
class Signup(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        if not username or not password:
            return JsonResponse({'error': 'Username and password are required.'}, status=400)

        try:
            user = User.objects.create_user(username=username, password=password,email=email)
            return JsonResponse({'message': 'User created successfully.'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class SignIn(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Username and password are required.'}, status=400)

        user = authenticate(request, username=username, password=password)
        print("USER",user.id)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful.', 'username': user.username, 'user_id':user.id}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials.'}, status=401)


@method_decorator(csrf_exempt, name='dispatch')
class MessageView(View):
    def get(self, request):
        messages = Messages.objects.all().values('id', 'user__username', 'message', 'created_on')
        return JsonResponse(list(messages), safe=False)

    def post(self, request):
        data = json.loads(request.body)
        message = data.get('message')
        USER_ID =  int(data.get('user'))
        print(USER_ID)
        
        print(type(USER_ID))
        user = User.objects.get(pk=USER_ID)
        if message:
            new_message = Messages.objects.create(user = user,message=message)
            to_send = {
                'id': new_message.id,
                'message': new_message.message,
                'created_on': new_message.created_on,
                'user': new_message.user.username
            }
            print(to_send)
            return JsonResponse(to_send, status=201)

        return JsonResponse({'error': 'Message content is required.'}, status=400)
