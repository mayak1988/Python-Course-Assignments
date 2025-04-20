import sys

# Check for correct number of command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <height> <width>")
    sys.exit(1)

height = int(sys.argv[1])
width = int(sys.argv[2])

area = height * width
perimeter = 2 * (height + width)

print(f'The area of the rectangle is: {area}')
print(f'The perimeter of the rectangle is: {perimeter}')