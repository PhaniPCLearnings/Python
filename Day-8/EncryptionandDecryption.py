alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction=input("Choose your type: Encryption or Decryption : ").lower()
text=input("Choose your message : ").lower()
shift_Count=int(input("How many times you want to shift : "))
encrypted_value=[]
decrypted_value=[]
def encrypt(original_text,shift):
    for i in original_text:
        get_index=alphabet.index(i)
        index_updated=get_index + shift
        encrypted_value.append(alphabet[index_updated])
    return encrypted_value

def decrypt(original_text,shift):
    for i in original_text:
        get_index = alphabet.index(i)
        index_updated=get_index - shift
        decrypted_value.append(alphabet[index_updated])
    return decrypted_value


if direction=='encryption':
    enc_value=encrypt(text,shift_Count)
    enc_text=''
    for i in enc_value:
        enc_text+=i
    print(f"Here is your encrypted Text : {enc_text}")
elif direction=='decryption':
    dec_value=decrypt(text,shift_Count)
    dec_text=''
    for i in dec_value:
        dec_text+=i
    print(f"Here is your Decryted Text : {dec_text}")
else:
    print("Invalid Input")
