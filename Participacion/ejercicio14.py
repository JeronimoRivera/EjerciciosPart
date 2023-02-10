nums = []
print("Cuantos numeros ingresara? ")
n = int(input())
i = 0
while i < n:
    print ("El valor numero: ", i + 1 )
    val = float(input())
    nums.append(val)
    i += 1
prom = sum(nums) / len(nums)
print("La media aritmetica es: ",prom)