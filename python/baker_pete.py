def cakes(recipe, available):
    flag = 0
    if all(x in available.keys() for x in recipe.keys()):
        flag = 1
    quantity = []
    if flag:
        for key in recipe:
            quantity.append(available[key] // recipe[key])
        return min(quantity)
    return 0


if __name__ == '__main__':
    users_recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    users_available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(cakes(recipe=users_recipe, available=users_available))
