from models import FoodPrice

with open('./food_price_input.csv', 'r') as input_file:
    for line in input_file.readlines():
        data = line.split(',')
        new_food = FoodPrice(ndb_no=data[0],
                cents=data[2]*100,
                units=1,
                unit_name=data[1])
        new_food.save()
