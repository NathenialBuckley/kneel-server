METALS = [
    {
        "id": 1,
        "metal": "Sterling Silver",
        "price": 12.42
    },
    {
        "id": 2,
        "metal": "14K Gold",
        "price": 736.4
    },
    {
        "id": 3,
        "metal": "24K Gold",
        "price": 1258.9
    },
    {
        "id": 4,
        "metal": "Platinum",
        "price": 795.45
    },
    {
        "id": 5,
        "metal": "Palladium",
        "price": 1241
    }
]


def get_all_metals():
    return METALS


def create_metals(metal):
    max_id = METALS[-1]["id"]
    new_id = max_id + 1
    metal["id"] = new_id
    METALS.append(metal)
    return metal


def delete_metal(id):
    # Initial -1 value for animal index, in case one isn't found
    metal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, metal in enumerate(METALS):
        if metal["id"] == id:
            # Found the animal. Store the current index.
            metal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if metal_index >= 0:
        METALS.pop(metal_index)
