def change_password(password):
    old = 'WalterSande'
    new = password
    
    if new == old:
        print("\nA nova senha não pode ser igual à antiga.")
        
        return False
    else:
        print("\nNova senha: {}".format(new))

        return True

password = str(input("Digite a nova senha: "))
change_password(password)
