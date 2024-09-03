import os
import inspect





def get_caller_script_path():
    frame = inspect.stack()[-1]
    module = inspect.getmodule(frame[0])    
    if module is None:
        return None   
    caller_file = os.path.abspath(module.__file__)    
    return caller_file

def get_caller_script_directory():
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    
    if module is None:
        return None

    caller_file = module.__file__
    
    caller_directory = os.path.dirname(os.path.abspath(caller_file))
    
    return caller_directory




def remove_key(name, ID):
    directory = get_caller_script_path()
    key = "NO KEY"
    security_level = "NO SECURITY LEVEL"
    password = "NO PASSWORD"
    response = "Error: Unknow Error"
    try:        
        file = open("/opt/wallet/requests/request.txt", "w")
        content = f"remove\n{name}\n{key}\n{ID}\n{security_level}\n{directory}\n{password}\n"
        file.write(content)
        file.close()
        print("Waiting for response")
        path = os.path.dirname(directory)
        response = path + "/respose.txt"
        print(response)
        while True:
            try:
                with open(response) as file:
                    file_content = file.read()
                    break
                  
            except:
                print("Waiting for response...")   
       
        os.remove(response)

                
    except:
        print("Errore durante la ricezione della chiave")   
            
    if file_content == "Wrong Directory":
        response = "Error: Program directory is different"
    elif file_content == "no name":
        response = "Error: key name not found"
    elif file_content == "wrong password":
        response = "Error: wrong password"
    elif file_content == "access denied":
        response = "Error: Request denied by user"
    elif file_content == "Index missing":
        response = "Error: File index missing. Did you alredy put a key in the wallet?"
    elif file_content == "password cancelled":
        response = "Error: Operation cancelled by user"
    elif file_content == "wrong id":
        response = "Error: Wrong ID"
    else:
        response = file_content



def put_key(name, key, ID, security_level, password):
    directory = get_caller_script_path()
            
    file = open("/opt/wallet/requests/request.txt", "w")
    content = f"put\n{name}\n{key}\n{ID}\n{security_level}\n{directory}\n{password}\n"
    file.write(content)
    file.close()
    print("Chiave inviata")
    #print("Errore durante l'invio della chiave")


def get_key(name, ID):
    directory = get_caller_script_path()
    key = "NO KEY"
    security_level = "NO SECURITY LEVEL"
    password = "NO PASSWORD"
    response = "Error: Unknow Error"
    try:        
        file = open("/opt/wallet/requests/request.txt", "w")
        content = f"get\n{name}\n{key}\n{ID}\n{security_level}\n{directory}\n{password}\n"
        file.write(content)
        file.close()
        print("Waiting for key")
        path = os.path.dirname(directory)
        response = path + "/respose.txt"
        print(response)
        while True:
            try:
                with open(response) as file:
                    encrypted_key = file.read()
                    break
                  
            except:
                print("Waiting for key...")   
       
        os.remove(response)

                
    except:
        print("Errore durante la ricezione della chiave")   
             

    
        
    return encrypted_key