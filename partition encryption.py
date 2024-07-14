from cryptography.fernet import Fernet; import os, base64, subprocess, shutil

def create_vhd(drive_letter, target_path, size_mb): # a          
    try:
        with open(f"create_vhd.txt", "w") as f:
            
            f.write(f"""
create vdisk file={target_path} maximum={size_mb} type=fixed
attach vdisk
create partition primary
format fs=ntfs quick
assign letter={drive_letter[0]}
exit
            """)
            
        subprocess.run(["diskpart", "/s", "create_vhd.txt"])
        print(f"Virtual drive {drive_letter} created successfully at {target_path}.")
        os.remove(f"create_vhd.txt")
        
        with open(f"{drive_letter}\\$DO_NOT_DELETE.data", "w") as f: # marks disk a virtual drive
            f.write("")
            
        if os.path.isfile("partition_list.data"):
            with open("partition_list.data", "a") as f:
                f.write(f"\n{target_path} - {drive_letter}")
        else:
            with open("partition_list.data", "w") as f:
                f.write(f"{target_path} - {drive_letter}")   
            
    except Exception as e:
        print(f"Failed to create virtual drive {drive_letter} at {target_path}.")
        print(e)
        

def remove_vhd(drive_letter, target_path): # b
    try:
        with open("remove_vhd.txt", "w") as f:
            f.write(f"""
select vdisk file={target_path}
detach vdisk
delete vdisk file={target_path}
            """)
            
        subprocess.run(["diskpart", "/s", "remove_vhd.txt"])
        print(f"Virtual drive {drive_letter} at {target_path} removed successfully.")
        os.remove("remove_vhd.txt")
        try:
            with open("partition_list.data", "r+") as f:
                read_data = f.read()
                read_data_list = read_data.split("\n")
                temp = []
                for i in read_data_list:
                    if target_path not in i:
                        temp.append(i)
                to_write = "\n".join(temp)
                f.write(to_write)
                
        except Exception as e:
            print(e)
            
    except Exception as e:
        print(f"Failed to remove {drive_letter} at {target_path}\n{e}")   
      
      
def get_used_size(drive_letter):
    total_used_size = 0
    for path, dirs, files in os.walk(drive_letter):
        for file in files:
            total_used_size += os.path.getsize(os.path.join(path, file))
    return total_used_size
      
      
def encrypt_drive(drive_letter): # c
    drive_size = get_used_size(drive_letter)
    encrypted_size = 0
    # encrypt all files
    for path, dirs, files in os.walk(drive_letter, topdown=False):
        for file in files:
            encrypted_size += os.path.getsize(os.path.join(path, file))
            print(f"Encrypting: {file} {round(os.path.getsize(os.path.join(path, file))/1024, 2)}KB | {round(encrypted_size/1024**3, 4)}GB / {round(drive_size/1024**3, 4)}GB")

            with open(os.path.join(path, file), "rb") as f:
                data = f.read()
            os.remove(os.path.join(path, file))
            
            with open(os.path.join(path, file), "wb") as f:
                f.write(Fernet(key).encrypt(data))
            
    # rename all files
    for path, dirs, files in os.walk(drive_letter, topdown=False):
        
        for dir in dirs:
            print(f"Renaming: '{dir}' to '{ec(dir)}'")
            try:
                os.rename(os.path.join(path, dir), os.path.join(path, ec(dir)))
            except:
                print("Failed ^^^")
            
        for file in files:
            print(f"Renaming: '{file}' to '{ec(file)}'")
            try:
                os.rename(os.path.join(path, file), os.path.join(path, ec(file)))
            except:
                print("Failed ^^^")


def decrypt_drive(drive_letter): # d
    inv = False         
    # decrypt all files
    drive_size = get_used_size(drive_letter)
    decrypted_size = 0
    for path, dirs, files in os.walk(drive_letter, topdown=False):
        for file in files:
            decrypted_size += os.path.getsize(os.path.join(path, file))
            if inv == True:
                break
            print(f"Decrypting: {dc(file)} {round(os.path.getsize(os.path.join(path, file))/1024, 2)}KB | {round(decrypted_size/1024**3, 4)}GB / {round(drive_size/1024**3, 4)}GB")
            
            with open(os.path.join(path, file), "rb") as f:
                data = f.read()
            os.remove(os.path.join(path, file))
            
            with open(os.path.join(path, file), "wb") as f:
                try:
                    f.write(Fernet(key).decrypt(data))
                except:
                    print("Invalid key")
                    inv = True
                    
    # rename all files
    for path, dirs, files in os.walk(drive_letter, topdown=False):
        
        for dir in dirs:
            print(f"Renaming: '{dir}' to '{dc(dir)}'")
            try:
                os.rename(os.path.join(path, dir), os.path.join(path, dc(dir)))
            except:
                print("Failed ^^^")
        for file in files:
            print(f"Renaming: '{file}' to '{dc(file)}'")
            try:
                os.rename(os.path.join(path, file), os.path.join(path, dc(file)))
            except:
                print("Failed ^^^")   


def mount_vhd(vhd_path, drive_letter):
    with open("mount_vhd.txt", "w") as f:
        
        f.write(f"""
select vdisk file={vhd_path}
attach vdisk
assign letter={drive_letter}
exit
        """)
        
    subprocess.run(["diskpart", "/s", "mount_vhd.txt"])
    os.remove("mount_vhd.txt")


def unmount_vhd(vhd_path):
    with open('unmount_vhd.txt', 'w') as f:
        
        f.write(f"""
select vdisk file={vhd_path}
detach vdisk
exit
        """)
        
    subprocess.run(['diskpart', '/s', 'unmount_vhd.txt'])
    os.remove("unmount_vhd.txt")


def display_drives():
    try:
        with open("partition_list.data", "r") as f:
            print(f.read())
    except Exception as e:
        print(e)
        
        
def clear_vhd(drive_letter):
    if input(f"Enter 'cOnFiRm!' if you are sure you want to delete {drive_letter}?: ") == "cOnFiRm!":
        for path, dirs, files in os.walk(drive_letter):
            
            for file in files:
                if file != "$DO_NOT_DELETE.data":
                    print(f"Deleting: {file}")
                    try:
                        os.remove(os.path.join(path, file))
                    except:
                        print("Failed ^^^")
            for dir in dirs:
                print(f"Detining: {dir}")
                try:
                    shutil.rmtree(os.path.join(path, dir))
                except:
                    print("Failed ^^^")
    else:
        print("Ending process")

def ec(name):
    if name != "$DO_NOT_DELETE.data":
        local_key = str(key)[2:12]
        encrypted_name = []
        name = list(name)
        for i in range(len(name)):
            if name[i].isalpha(): # if character is a-z / A-Z
                if name[i] == name[i].upper(): # if character is uppercase
                    letter = "A"
                else: # if character is lower case
                    letter = "a"
                encrypted_name.append(chr((((ord(name[i]) + ord(local_key[i % len(local_key)])) - (2 * ord(letter))) % 26) + ord(letter)))
            else:
                encrypted_name.append(name[i])
        return "".join(encrypted_name)


def dc(name):
    if name != "$DO_NOT_DELETE.data":
        local_key = str(key)[2:12]
        decrypted_name = []
        name = list(name)
        for i in range(len(name)):
            if name[i].isalpha(): # if character is a-z / A-Z
                if name[i] == name[i].upper(): # if character is uppercase
                    letter = "A"
                else: # if character is lower case
                    letter = "a"
                decrypted_name.append(chr(((ord(name[i]) - ord(local_key[i % len(local_key)])) % 26) + ord(letter)))
            else:
                decrypted_name.append(name[i])
        return "".join(decrypted_name)



def get_key():
    global key
    key = input("Key? (password): ").encode("utf-8")

    if len(key) < 32:
        key = key + b'\0' * (32 - len(key) - 1) + b"="
    elif len(key) > 32:
        key = key[:32] + b"="
        
    key = base64.urlsafe_b64encode(key)



choice = " "
while ord(choice.upper()) < ord("A") or ord(choice.upper()) > ord("H"):
    choice = input("""Options:  
    a) Create a drive
    b) Delete a drive
    c) Encrypt a drive
    d) Decrypt a drive
    e) Mount a drive
    f) Unmount a drive
    g) Clear a drive
    h) List drives
    """)                                # chose options 
    if ord(choice.upper()) < ord("A") or ord(choice.upper()) > ord("H"):
        print("Invalid input\n")

inp = ""
while inp.isalpha() == False and choice != "h": # chose drive
    inp = input("Drive letter (A-Z): ")
    drive_letter = inp.upper() + ":"
    if os.path.exists(drive_letter) == False and choice not in ["a", "e", "b"]:
        print("Drive does not exist, try another drive or create a drive first.")
        inp = ""
            
            
halt = False

if choice == "a":
    size_mb = int(input("Virtual drive size? (MB): "))
    target_path = input("Target path (e.g: 'C:\\VirtualDrive'): ") + ".vhd"
    create_vhd(drive_letter, target_path, size_mb)
   
   
if choice not in ["a", "b", "e", "h"] and os.path.isfile(f"{drive_letter}\\$DO_NOT_DELETE.data") == False:
    print("This doesn't look like a virtual drive, to reduce the likelyhood of permanent damage, you cannot proceed on drive", drive_letter)   
    halt = True
    
    
if halt == False:   
    if choice == "b":
        target_path = input("Target path (e.g: 'C:\\VirtualDrives'): ") + ".vhd"
        if input(f"Enter 'cOnFiRm!' if you are sure you want to delete {drive_letter} stored in {target_path}?: ") == "cOnFiRm!":
            remove_vhd(drive_letter, target_path)
        else:
            print("Ending process")
        
    elif choice == "c":
        get_key()
        encrypt_drive(drive_letter)
        
    elif choice == "d":
        get_key()
        decrypt_drive(drive_letter)

    if choice in ["e", "f"] :
        vhd_path = input("Virtual drive path (e.g: 'C:\\VirtualDrives'): ") + ".vhd"

    if choice == "e":
        mount_vhd(vhd_path, drive_letter)
    
    elif choice == "f":
        unmount_vhd(vhd_path)
        
    elif choice == "g":
        clear_vhd(drive_letter)
        
    elif choice == "h":
        display_drives()
     
print("\nFinished")