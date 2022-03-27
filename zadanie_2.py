phones =[
  {'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
  {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, 
  {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

phones.sort(key=lambda phone: phone['make']);
print(phones);