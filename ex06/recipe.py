cookbook = {
    "bocadillo": {
        "ingredients": ["jamón", "pan", "queso", "tomate"],
        "meal": "almuerzo",
        "prep_time": 10
    },
    "tarta": {
        "ingredients": ["harina", "azúcar", "huevos"],
        "meal": "postre",
        "prep_time": 60
    },
    "ensalada": {
        "ingredients": ["aguacate", "rúcula", "tomates", "espinacas"],
        "meal": "almuerzo",
        "prep_time": 15
    }
}

def print_recipe_names():
    print("Lista de recetas:")
    for recipe in cookbook:
        print("- " + recipe)

def print_recipe(recipe_name):
    recipe = cookbook.get(recipe_name)
    if recipe:
        print(f"Receta para {recipe_name}:")
        print(f"Lista de ingredientes: {recipe['ingredients']}")
        print(f"Tipo de comida: {recipe['meal']}")
        print(f"Tiempo de preparación: {recipe['prep_time']} minutos")
    else:
        print("La receta no existe en el recetario.")

def add_recipe():
    name = input("Ingrese el nombre de la receta: ")
    ingredients = input("Ingrese los ingredientes (separados por comas): ").split(", ")
    meal = input("Ingrese el tipo de comida: ")
    prep_time = int(input("Ingrese el tiempo de preparación (en minutos): "))
    cookbook[name] = {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}
    print(f"La receta {name} ha sido agregada al recetario.")

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(f"La receta {recipe_name} ha sido eliminada del recetario.")
    else:
        print("La receta no existe en el recetario.")

def print_cookbook():
    for recipe_name, recipe in cookbook.items():
        print_recipe(recipe_name)
        print()

def main():
    print("¡Bienvenido al recetario de Python!")
    while True:
        print("Lista de opciones:")
        print("1: Agregar una receta")
        print("2: Eliminar una receta")
        print("3: Ver una receta")
        print("4: Ver todo el recetario")
        print("5: Salir")
        option = input("Ingrese la opcion deseada: ")
        if option == "1":
            add_recipe()
        elif option == "2":
            recipe_name = input("Ingrese el nombre de la receta que desa eliminar: ")
            delete_recipe(recipe_name)
        elif option == "3":
            recipe_name = input("Ingrese el nombre de la receta que desea ver: ")
            print_recipe(recipe_name)
        elif option == "4":
            print_cookbook()
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no valida. Intente de nuevo")

if __name__ == '__main__':
    main()