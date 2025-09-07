alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
       
       if encode_or_decode == "decode":
           shift_amount *= -1

       shifted_position = alphabet.index(letter) + shift_amount
       # fixed shift of z or similar that gives Index error : list out of range 
       #    shifted_position = shifted_position % len(alphabet)
       shifted_position %= len(alphabet)
       output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result :  {output_text}")

caeser(original_text=text, shift_amount=shift, encode_or_decode=direction)