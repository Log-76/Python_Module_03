import sys

print("=== Command Quest ===")
print()
if len(sys.argv) == 1:
    print("No arguments provided!")
    print("Program name: " + sys.argv[0])
    print(f"Total arguments: {len(sys.argv)}")
else:
    i = 1
    print(f"Arguments received {len(sys.argv)-1}")
    while i < len(sys.argv):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {len(sys.argv)}")
