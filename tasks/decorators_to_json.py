def to_json(func_to_decorate):
    def wrapper():
        import json
        updating = func_to_decorate()
        updating = json.dumps(updating)
        return updating

    return wrapper



#@to_json
#def get_data():
#    return {
#        'data111': 4444
#   }
#print(get_data() )

