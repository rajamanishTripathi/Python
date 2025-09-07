alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                shift_amount *= -1
                
    for letter in original_text:
       if letter not in alphabet:
          output_text += letter
       else:
            shifted_position = alphabet.index(letter) + shift_amount

            # fixed shift of z or similar that gives Index error : list out of range 
            # shifted_position = shifted_position % len(alphabet)
            shifted_position %= len(alphabet)

            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result :  {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    run = input("if you want to encode or decode then type \"Yes\" otherwise type \"No\" .").lower()

    if run == "no":
        should_continue == False
        print("Good Bye !!!!!")