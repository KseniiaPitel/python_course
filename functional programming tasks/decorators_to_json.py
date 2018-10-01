from functools import wraps


def to_json(func_to_decorate):
    @wraps(func_to_decorate)
    def wrapper(*args, **kwargs):
        import json
        updating = func_to_decorate(*args, **kwargs)
        updating = json.dumps(updating)
        return updating

    return wrapper

"""
@to_json
def get_data():
    return {
        'data111': 4444
    }


print(get_data())
print(get_data.__name__)
print(get_data.__doc__)
"""