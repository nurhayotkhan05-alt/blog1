raja_shivaji = {
    "Riteish Deshmukh" : "Chhatripati Shivaji",
    "Salman Khan" : "Jeeva Mahala",
    "Sanjay Dutt" : "Afzal Khan",
    "Genelia Deshmukh" : "Rani Saibai"
}


x = raja_shivaji["Genelia Deshmukh"]
print(f"Genelia Deshmukh {x} rolida o'yndid!")

k = raja_shivaji.get("Riteish Deshmukh")
print(f"Riteish Deshmukh as {k}")


keys = raja_shivaji.keys()
print(keys)

v = raja_shivaji.values()
print(v)

raja_shivaji["Genelia Deshmukh"] = "Saibai"
print(raja_shivaji.values())