from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    "return the pygal 2-digit country code for a specifc country"
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #if not found, return none
    return None
  
#testing
'''  
print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
''' 