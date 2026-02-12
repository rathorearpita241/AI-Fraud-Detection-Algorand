from algosdk import account, encoding

private_key, address = account.generate_account()

print("ADDRESS:", address)
print("PRIVATE KEY:", private_key)
print("Address length:", len(address))
print("Valid Algorand address:", encoding.is_valid_address(address))
