# Q2:
# Count Even and Odd Numbers
# Take a list of numbers as input (comma-separated).
# Count how many are even and how many are odd.
# Print results.
# Example Input:
# 10, 21, 4, 7, 8

Nlist=input("Enter list of numbers: ")
nums=Nlist.split(",")
odd=0
even=0
for n in nums:
    if int(n)%2==0:
        even+=1
    else:
        odd+=1

print("Number of EVEN numbers: ",even)
print("Number of ODD numbers: ",odd)
