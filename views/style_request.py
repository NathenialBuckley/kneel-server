STYLES = [
    {
        "id": 1,
        "style": "Classic",
        "price": 10
    },
    {
        "id": 2,
        "style": "Modern",
        "price": 20
    },
    {
        "id": 3,
        "style": "Vintage",
        "price": 30
    }
]


def get_all_styles():
    return STYLES


def create_styles(style):
    max_id = STYLES[-1]["id"]
    new_id = max_id + 1
    style["id"] = new_id
    STYLES.append(style)
    return style


def delete_style(id):
    # Initial -1 value for animal index, in case one isn't found
    style_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, style in enumerate(STYLES):
        if style["id"] == id:
            # Found the animal. Store the current index.
            style_index = index

    # If the animal was found, use pop(int) to remove it from list
    if style_index >= 0:
        STYLES.pop(style_index)
