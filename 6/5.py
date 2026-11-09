raja_shivaji = {
    "Riteish Deshmukh" : "Chhatripati Shivaji",
    "Salman Khan" : "Jeeva Mahala",
    "Sanjay Dutt" : "Afzal Khan",
    "Genelia Deshmukh" : "Rani Saibai",
    "Riaan Deshmukh": "noname",
    "Abhishek" : "Sambhaji"
}


for x in raja_shivaji:
    print(x,end=" ")
print("\n")
for x in raja_shivaji:
    print(raja_shivaji[x],end=" ")
print("\n")
for x in raja_shivaji.values():
    print(x)
print("\n")

for x in raja_shivaji.keys():
    print(x)

print("\n")

for x in raja_shivaji.items():
    print(x,end=" ")