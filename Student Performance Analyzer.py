name = "Jahnavi"
n = int(input("Enter number of students: "))

marks = [0] * n

for i in range(n):
    marks[i] = int(input("Enter mark: "))

valid_count = 0
fail_count = 0

for m in marks:

    special = ""
    if name[0].lower() == 'j' and m % 5 == 0:
        special = " (Special)"

    if m < 0 or m > 100:
        print(m, "→ Invalid")

    else:
        valid_count += 1

        if m >= 90:
            print(m, "→ Excellent" +  special)

        elif m >= 75:
            print(m, "→ Very Good" +  special)

        elif m >= 60:
            print(m, "→ Good" +  special)

        elif m >= 40:
            print(m, "→ Average" +  special)

        else:
            print(m, "→ Fail" +  special)
            fail_count += 1

print("Total Valid Students:", valid_count)
print("Total Failed Students:", fail_count)
