
# while loop

count = 0
while count < 1000000:
    print("Looping", count)
    count = count + 1
    if count == 200000:
        break
    else:
        continue

