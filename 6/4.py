raja_shivaji = {
    "Riteish Deshmukh" : "Chhatripati Shivaji",
    "Salman Khan" : "Jeeva Mahala",
    "Sanjay Dutt" : "Afzal Khan",
    "Genelia Deshmukh" : "Rani Saibai",
    "Riaan Deshmukh": "noname",
    "Abhishek" : "Sambhaji"
}

raja_shivaji.pop('Riaan Deshmukh')
print(raja_shivaji)

raja_shivaji.popitem()
print(raja_shivaji)

del raja_shivaji["Sanjay Dutt"]
print(raja_shivaji)


raja_shivaji.clear()
print(raja_shivaji)


del raja_shivaji
print(raja_shivaji)