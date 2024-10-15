#write functions here, don't add input('') statements here!
def test_config():
    return True


def get_assessment_value(value):
    assess = value * 0.6
    return assess

def get_tax_assessed(value):
    tax = (value/100) * 0.72
    return round(tax, 2)
