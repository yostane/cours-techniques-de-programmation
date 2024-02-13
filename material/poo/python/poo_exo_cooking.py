class Ingredient:
    def __init__(self, name, state, unit, quantity):
        self.name = name
        self.state = state
        self.unit = unit
        self.quantity = quantity

    def equals(self, ingredient):
        if self.name == ingredient.name and self.state == ingredient.state:
            return True
        return False

    def __eq__(self, __value):
        return self.equals(__value)


class Dish:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __eq__(self, __value) -> bool:
        if len(self.ingredients) != len(__value.ingredients):
            return False
        # On clone les ingrédients pour qu'on puisse éliminer ceux qu'on retouve dans le premier plat
        ingredients_to_compare = __value.ingredients[:]
        for ingredient in self.ingredients:
            for i in range(len(ingredients_to_compare)):
                # Dès qu'on retrouve un ingrédient dans les deux plats on l'enlève
                if ingredients_to_compare[i] == ingredient:
                    del ingredients_to_compare[i]
                    break
        # Si on a vidé la liste, càd que tous les ingédients existents dans les deux plats
        if len(ingredients_to_compare) == 0:
            return True
        return False


ingredient_choucroute1 = Ingredient("Choucroute", "cooked", "g", 500)
ingredient_choucroute2 = Ingredient("Choucroute", "cooked", "kg", 1)
lard = Ingredient("Lard", "cooked", "g", 150)

print(ingredient_choucroute1 == ingredient_choucroute2)
print(ingredient_choucroute1 == lard)

choucroute = Dish(
    "Choucroute",
    [
        ingredient_choucroute1,
        lard,
        Ingredient("Saucisse entière", "cooked", "cadrinality", 2),
    ],
)

choucroute_light = Dish(
    "Choucroute light",
    [ingredient_choucroute1],
)

choucroute_double = Dish(
    "Choucroute",
    [
        ingredient_choucroute2,
        lard,
        Ingredient("Saucisse entière", "cooked", "cadrinality", 4),
    ],
)

print(choucroute_light == choucroute)
print(choucroute == choucroute_double)
