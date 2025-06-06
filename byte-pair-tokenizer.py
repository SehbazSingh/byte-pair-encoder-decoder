import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")

while True:
    menu = input("\nEnter a menu item (1 for encoding, 2 for decoding, q to quit): ").strip()

    if menu == "1":
        text = input("Enter text to encode: ")
        integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
        print("Encoded tokens:", integers)
    elif menu == "2":
        try:
            integers = input("Enter integers to decode (comma-separated): ")
            integers = list(map(int, integers.split(",")))
            strings = tokenizer.decode(integers)
            print("Decoded text:", strings)
        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")
    elif menu.lower() == "q":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please enter 1, 2, or q.")
