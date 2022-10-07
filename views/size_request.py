SIZES = [
    {
        "id": 1,
        "size": 0.5,
        "price": 5
    },
    {
        "id": 2,
        "size": 0.75,
        "price": 10
    },
    {
        "id": 3,
        "size": 1,
        "price": 15
    },
    {
        "id": 4,
        "size": 1.5,
        "price": 20
    },
    {
        "id": 5,
        "size": 2,
        "price": 25
    }
]


def get_all_sizes():
    return SIZES


def create_sizes(size):
    max_id = SIZES[-1]["id"]
    new_id = max_id + 1
    size["id"] = new_id
    SIZES.append(size)
    return size


def delete_size(id):
    # Initial -1 value for animal index, in case one isn't found
    size_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, size in enumerate(SIZES):
        if size["id"] == id:
            # Found the animal. Store the current index.
            size_index = index

    # If the animal was found, use pop(int) to remove it from list
    if size_index >= 0:
        SIZES.pop(size_index)
