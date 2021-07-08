def user_to_response(user_model):
    fields = [
        'email', 'username', 'first_name', 'last_name', 'date_joined',
        'last_login', 'is_superuser'
    ]
    user = {'password': '0000000000'}
    for field in fields:
        user[field] = getattr(user_model, field)
    return user