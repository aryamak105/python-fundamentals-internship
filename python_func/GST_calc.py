#GST Calculator......

amount = float(input("Enter Amount: "))
gst = float(input("Enter GST %: "))

choice = input("Add or Remove GST (A/R): ")

if choice == "A":
    total = amount + (amount * gst / 100)
    print("Price after GST =", total)

elif choice == "R":
    original = amount * 100 / (100 + gst)
    print("Price without GST =", original)

else:
    print("Invalid Choice")