def shutdown(user_input):
    if user_input == "Yes":
        return "Shutting Down"
    elif user_input == "no":
        return "Abort Shut Down"
    else:
        return "Sorry"
    
print(shutdown("Yes"))   
print(shutdown("no"))    
print(shutdown("maybe"))
