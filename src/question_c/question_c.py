#write functions here, don't add input('') statements here!
def test_config():
    return True


def get_bonus_pay_amount(sales):
    if(0 <= sales and sales < 500): return round(sales * 0.05, 2)
    elif(500 <= sales and sales < 1000): return round(sales * 0.06, 2)
    elif(1000 <= sales and sales < 1500): return round(sales * 0.07, 2)
    elif(1500 <= sales and sales < 2000): return round(sales * 0.08, 2)
    else: return "Invalid arguments"