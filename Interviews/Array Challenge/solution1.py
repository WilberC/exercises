def ArrayChallenge(arr):
    return arr if arr[0] == 0 else ''.join(str(item) for item in arr[arr[0]::] + arr[:arr[0]])


# print(ArrayChallenge(raw_input()))
