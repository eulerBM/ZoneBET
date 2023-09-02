def user_on(user):
    if user.is_authenticated:
        return user.dados.money
    else:
        return 0