#Task  check the user email and
#passowrd is correct then give us all information of user
Name ="Haram Hussain"
fn = "M.younus"
Age ="20"
Email ="haramchohan928@gmail.com"
password = "haram123"
phoneNo ="03183656928"
useremail = input("Enter your Email ")
userpass = input("Enter your Password")
if Email == useremail and password ==userpass : 
    print("Name :",Name)
    print("Father Name ",fn)
    print("Age",Age )
    print ("Email", Email )
    print("password :", password)
    print ("Phone Number :",phoneNo)
else :
    print ("Give us Correct Information ")
