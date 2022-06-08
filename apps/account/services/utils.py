from django.core.mail import send_mail


def send_activate_code(activate_code: str, email: str):
    title = "Hello, follow the link to activate Your account"
    message = f"Please click link for activate account http://127.0.0.1:8000/api/v1/account/activate/{activate_code}/"
    from_email = "Happyshop.kg"

    send_mail(
        title,
        message,
        from_email,
        [email],
        fail_silently=False,
    )


def send_new_password(email, new_password):

    title = 'Your account password was reset.'
    message = f'Hello, it is Your new password: {new_password} on email: {email}'
    from_email = "Happyshop.kg"

    send_mail(
            title,
            message,
            from_email,
            [email],
            fail_silently=False,
        )