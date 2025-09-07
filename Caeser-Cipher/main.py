alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    listing = list(text)
    # print(listing)
    output_listing = []
    for i in listing:
        if i in alphabet:
            character_index = alphabet.index(i)
            listing_output_index = character_index+shift
            listing_output_index_value = alphabet[listing_output_index]
            # print(listing_output_index_value)
            output_listing.append(listing_output_index_value)
        else:
            print("Enter valid characters")

    # print(output_listing)
    encrypt_output = "".join(output_listing)
    # print(encrypt_output)

encrypt()

def decrypt():
    text = input("Type your message to decrypt:\n").lower()
    shift = int(input("Type the shift number to decrypt:\n"))
    listing = list(text)
    # print(listing)
    output_listing = []
    for i in listing:
        if i in alphabet:
            character_index = alphabet.index(i)
            listing_output_index = character_index-shift
            listing_output_index_value = alphabet[listing_output_index]
            # print(listing_output_index_value)
            output_listing.append(listing_output_index_value)
        else:
            print("Enter valid characters to decrypt")

    # print(output_listing)
    decrypt_output = "".join(output_listing)
    print(f"Decrypted Message: {decrypt_output}")

decrypt()