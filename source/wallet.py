from cryptography.fernet import Fernet
import os
from random import randint
import sys
import hashlib
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def write_key():
    
    key = Fernet.generate_key()
    f = Fernet(key)
    with open("key.key", "wb") as key_file:
        key_file.write(key)



def load_key():   
    return open("key.key", "rb").read()




def put_key():
    wallet_key = load_key()
    f = Fernet(wallet_key)

    if not os.path.isfile("index.txt"):    
        with open("index.txt", "w") as file:
            pass

    with open("index.txt", "r") as index_file:
        pippo = index_file.read()

    while True:
        caso = str(randint(10000, 99999))
        if caso not in pippo:
            break

    with open("index.txt", "a") as index_file:
        index_file.write(name + ":" + caso + "\n")

    filename = "keys/" + caso + ".txt"
    with open(filename, "w") as file:
        file.write(name + '\n')
        file.write(key + '\n')
        file.write(ID + '\n')
        file.write(security_option + '\n')
        file.write(directory + '\n')

        if "2" in security_option or "3" in security_option:
            BUF_SIZE = 32768  # Read file in 32kb chunks
            md5 = hashlib.md5()
            sha1 = hashlib.sha1()
            with open(directory, 'rb') as fi:
                while True:
                    data = fi.read(BUF_SIZE)
                    if not data:
                        break
                    md5.update(data)
                    sha1.update(data)
            if "2" in security_option:
                file.write(sha1.hexdigest() + '\n')
            else:
                file.write("NO HASH\n")
            if "3" in security_option:
                file.write(md5.hexdigest() + '\n')
            else:
                file.write("NO MD5\n")
        else:
            file.write("NO HASH\n")
            file.write("NO MD5\n")

        if "4" in security_option:            
            file.write(password)
        else:
            file.write("NO PASSWORD\n")
    
    with open(filename, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    
    
    return "Save complete"

def get_key():
    wallet_key = load_key()
    f = Fernet(wallet_key)

    path = os.path.dirname(directory)
    path = path + "/respose.txt"
    print(path)

    key_code = None
    try:
        with open("index.txt", 'r') as file:
            for linea in file:
                if name + ':' in linea:
                    key_code = linea.split(':', 1)[1].strip()
                    break
    except:
        with open(path, "w") as file:
                        
            file.write("Index missing")
        return
    if key_code is None:
        print("No data found for the given name.")
        with open(path, "w") as file:                        
            file.write("Error: No name found")
            
        return

    dir_key = "keys/" + key_code + ".txt"
    with open(dir_key, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted_data = f.decrypt(encrypted_data).decode('utf-8')
    except Exception as e:
        print("Error decrypting data:", e)
        return

    
    temp_filename = dir_key + ".tmp"
    with open(temp_filename, "w") as file:
        file.write(decrypted_data)
    
    with open(temp_filename, "r") as file:
        decrypted_lines = file.readlines()

    os.remove(temp_filename)
    
    

   
   
    name_key = decrypted_lines[0]    
    name_key = name_key[:-1]

    

    ID_key = decrypted_lines[2]
    ID_key = ID_key[:-1]

    security_option_key = decrypted_lines[3]
    security_option_key = security_option_key[:-1]

    directory_key = decrypted_lines[4]
    directory_key =directory_key[:-1]

    HASH_key = decrypted_lines[5]
    HASH_key =HASH_key[:-1]

    MD5_key = decrypted_lines[6]
    MD5_key =MD5_key[:-1]

    password_key = decrypted_lines[7]
    password_key = password_key[:-1]

    





    #verifica autenticità
    if ID == ID_key:

        if "0" in security_option_key:
            key_key = decrypted_lines[1]
            key_key = key_key[:-1]
            with open(path, "w") as file:            
                file.write(key_key)
            auth_status = "True"
            return
            
        if "1" in security_option_key:
            if not directory == directory_key:
                print("Wrong Directory")       
        
                with open(path, "w") as file:
                    
                    file.write("WRONG Directory")
                return

        if "2" in security_option_key or "3" in security_option_key:
            BUF_SIZE = 32768  # Read file in 32kb chunks
            md5 = hashlib.md5()
            sha1 = hashlib.sha1()
            with open(directory, 'rb') as fi:
                while True:
                    data = fi.read(BUF_SIZE)
                    if not data:
                        break
                    md5.update(data)
                    sha1.update(data)
            md5 = md5.hexdigest()
            sha1 = sha1.hexdigest()

            print("MD5: "+md5+" "+MD5_key)
            print("HASH: "+sha1+" "+HASH_key)
            if "2" in security_option_key:
                if not HASH_key == sha1:
                    print("Wrong sha1")       
            
                    with open(path, "w") as file:                        
                        file.write("Error: Wrong sha1")
                    return
            if "3" in security_option_key:
                if not MD5_key == md5:
                    print("Wrong md5")       
            
                    with open(path, "w") as file:
                        
                        file.write("Error: Wrong md5")
                    return
        if "4" in security_option_key:           
            root = tk.Tk()
            root.withdraw()  
            password = simpledialog.askstring("Password Required", "Please enter your password for {}, requied by {}:".format(name, directory), show='*')
            
            if password is None:
                print("Operation canceled by the user")
                with open(path, "w") as file:
                    file.write("password cancelled")
                root.destroy()
                return

            if not password == password_key:               
                print("Wrong password")
                with open(path, "w") as file:
                    file.write("wrong password")
                root.destroy()
                return

            root.destroy() 
                

           
                

        if "5" in security_option_key:
            root = tk.Tk()
            root.title("Notifica")
            
            # Crea una label con il messaggio
            label = tk.Label(root, text="Key: {} is requied by: {}".format(name, directory), padx=20, pady=20)
            label.pack()
            
            # Imposta il tempo di chiusura (in millisecondi)
            root.after("3000", root.destroy)
            
            # Mostra la finestra
            root.mainloop()

        if "6" in security_option_key:
            root = tk.Tk()
            root.withdraw()  
            
            response = messagebox.askyesno("Wallet, confirm access to key", "Do you want to give {} key to {}?".format(name, directory))
            
            root.destroy()  

            if response:
                print("Request accepted")
            else:
                print("Access denied by user")
                with open(path, "w") as file:                        
                    file.write("access denied")
                return
        else:
            print("Wrong ID")
        
            with open(path, "w") as file:                        
                file.write("wrong id")
            return


      
        key_key = decrypted_lines[1]
        key_key = key_key[:-1]
        print(key_key)
        with open(path, "w") as file:            
            file.write(key_key)
 
def remove_key():
    wallet_key = load_key()
    f = Fernet(wallet_key)

    path = os.path.dirname(directory)
    path = path + "/respose.txt"
    print(path)

    key_code = None
    try:
        with open("index.txt", 'r') as file:
            for linea in file:
                if name + ':' in linea:
                    key_code = linea.split(':', 1)[1].strip()
                    break
    except:
        with open(path, "w") as file:
                        
            file.write("Index missing")
        return
    if key_code is None:
        print("No data found for the given name.")
        with open(path, "w") as file:
                        
            file.write("No name")
            
        return

    dir_key = "keys/" + key_code + ".txt"
    with open(dir_key, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted_data = f.decrypt(encrypted_data).decode('utf-8')
    except Exception as e:
        print("Error decrypting data:", e)
        return

    
    temp_filename = dir_key + ".tmp"
    with open(temp_filename, "w") as file:
        file.write(decrypted_data)
    
    with open(temp_filename, "r") as file:
        decrypted_lines = file.readlines()

    os.remove(temp_filename)
    
    

   
   
    name_key = decrypted_lines[0]    
    name_key = name_key[:-1]

    

    ID_key = decrypted_lines[2]
    ID_key = ID_key[:-1]

    security_option_key = decrypted_lines[3]
    security_option_key = security_option_key[:-1]

    directory_key = decrypted_lines[4]
    directory_key =directory_key[:-1]

    HASH_key = decrypted_lines[5]
    HASH_key =HASH_key[:-1]

    MD5_key = decrypted_lines[6]
    MD5_key =MD5_key[:-1]

    password_key = decrypted_lines[7]
    password_key = password_key[:-1]

    





    #verifica autenticità
    if ID == ID_key:

        if "0" in security_option_key:
            comando = "sudo rm -rf keys/{}.txt".format(key_code)
            print(comando)
            os.system(comando)
            with open("index.txt", 'r', encoding='utf-8') as file:
                lines = file.readlines()

                
                new_lines = [linea for linea in lines if linea.strip() != name+":"+key_code]

            
            with open("index.txt", 'w', encoding='utf-8') as file:
                file.writelines(new_lines)

            with open(path, "w") as file:            
                file.write("remove complete")
            return
            
        if "1" in security_option_key:
            if not directory == directory_key:
                print("Wrong Directory")       
        
                with open(path, "w") as file:
                    
                    file.write("WRONG Directory")
                return

        if "2" in security_option_key or "3" in security_option_key:
            BUF_SIZE = 32768  # Read file in 32kb chunks
            md5 = hashlib.md5()
            sha1 = hashlib.sha1()
            with open(directory, 'rb') as fi:
                while True:
                    data = fi.read(BUF_SIZE)
                    if not data:
                        break
                    md5.update(data)
                    sha1.update(data)
            md5 = md5.hexdigest()
            sha1 = sha1.hexdigest()

            print("MD5: "+md5+" "+MD5_key)
            print("HASH: "+sha1+" "+HASH_key)
            if "2" in security_option_key:
                if not HASH_key == sha1:
                    print("Wrong sha1")       
            
                    with open(path, "w") as file:                        
                        file.write("Error: Wrong sha1")
                    return
            if "3" in security_option_key:
                if not MD5_key == md5:
                    print("Wrong md5")       
            
                    with open(path, "w") as file:
                        
                        file.write("Error: Wrong md5")
                    return
        if "4" in security_option_key:           
            root = tk.Tk()
            root.withdraw()  
            password = simpledialog.askstring("Password Required", "Please enter your password for delete {}, requied by {}:".format(name, directory), show='*')
            
            if password is None:
                print("Operation canceled by the user")
                with open(path, "w") as file:
                    file.write("password cancelled")
                root.destroy()
                return

            if not password == password_key:               
                print("Wrong password")
                with open(path, "w") as file:
                    file.write("wrong password")
                root.destroy()
                return

            root.destroy() 
                

           
                

        if "5" in security_option_key:
            root = tk.Tk()
            root.title("Notify")
            
            # Crea una label con il messaggio
            label = tk.Label(root, text="Key delete: {} is requied by: {}".format(name, directory), padx=20, pady=20)
            label.pack()
            
            # Imposta il tempo di chiusura (in millisecondi)
            root.after("3000", root.destroy)
            
            # Mostra la finestra
            root.mainloop()

        if "6" in security_option_key:
            root = tk.Tk()
            root.withdraw()  
            
            response = messagebox.askyesno("Wallet, confirm remove key", "Do you want accept remove of {} key request {}?".format(name, directory))
            
            root.destroy()  

            if response:
                print("Request accepted")
            else:
                print("Access denied by user")
                with open(path, "w") as file:                        
                    file.write("access denied")
                return
        else:
            print("Wrong ID")
        
            with open(path, "w") as file:                        
                file.write("wrong id")
            return


      
        comando = "sudo rm -rf keys/{}".format(key_code)
        print(comando)
        os.system(comando)
        with open("index.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()

            
            new_lines = [linea for linea in righe if linea.strip() != nome+":"+key_code]

           
        with open("index.txt", 'w', encoding='utf-8') as file:
            file.writelines(new_lines)

        with open(path, "w") as file:            
            file.write("remove complete")
 



if os.path.isfile("key.key") == False:
    write_key()




while True:
    global key, ID, name, security_option, password
    if os.path.isfile("/opt/wallet/requests/request.txt") == True:
        file = open("/opt/wallet/requests/request.txt")
        print("File requests esistente")
            
        lines = file.readlines()
        tipe = lines[0]

        name = lines[1]    
        name = name[:-1]

        key = lines[2]
        key = key[:-1]

        ID = lines[3]
        ID = ID[:-1]

        security_option = lines[4]
        security_option = security_option[:-1]

        directory = lines[5]
        directory =directory[:-1]

        password = lines[6]
        #password =password[:-1]


        file.close()
        os.remove("/opt/wallet/requests/request.txt")

        if "get" in tipe:
            get_key()
        elif "put" in tipe:
            put_key()
        elif "remove" in tipe:
            remove_key()

        os.system("sudo find /opt/wallet/wallet -type d -exec chmod 700 {} +")
        os.system("sudo find /opt/wallet/wallet -type f -exec chmod 600 {} +")
    else:
        print("File requests non esistente")

    #exit()
    os.system("sleep 2")
