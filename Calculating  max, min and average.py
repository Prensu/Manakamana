list_num= []
while True:
    num= input("Enter a number (Enter 'done' to finish): ")
    if num == "done":
        break
    list_num.append(int(num))
print("Muximum=", max(list_num), "  Minimum=", min(list_num), "  Average:", sum(list_num)/len(list_num))

print("now the program is completed! ") 
