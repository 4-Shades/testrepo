def octal_to_binary(octal_str):
  decimal_value = int(octal_str, 8)
  binary_str = bin(decimal_value)[2:]
  return binary_str

octal_str = input("Enter an octal number: ")

binary_str = octal_to_binary(octal_str)

print("The binary equivalent is:", binary_str)