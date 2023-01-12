def generate_shopping_list(user, ingredients):
    for_user = f'Shopping list for: {user.get_full_name()}\n\n'
    shopping_list = '\n'.join([
        f'- {ingredient["ingredient__name"]} '
        f'({ingredient["ingredient__measurement_unit"]})'
        f' - {ingredient["amount"]}'
        for ingredient in ingredients
    ])
    shopping_cart = for_user + shopping_list
    return shopping_cart
