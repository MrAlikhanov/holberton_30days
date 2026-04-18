import random
import string

# 1. List of hexadecimal colors
def list_of_hexa_colors(count):
    colors = []
    for _ in range(count):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        colors.append(color)
    return colors

print(list_of_hexa_colors(3))  # ['#a3e12f', '#03ed55', '#eb3d2b']
print(list_of_hexa_colors(1))  # ['#b334ef']

# 2. List of RGB colors
def list_of_rgb_colors(count):
    colors = []
    for _ in range(count):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'rgb({r},{g},{b})')
    return colors

print(list_of_rgb_colors(3))  # ['rgb(5,55,175)', 'rgb(50,105,100)', 'rgb(15,26,80)']
print(list_of_rgb_colors(1))  # ['rgb(33,79,176)']

# 3. Generate colors — hexa or rgb
def generate_colors(color_type, count):
    if color_type == 'hexa':
        return list_of_hexa_colors(count)
    elif color_type == 'rgb':
        return list_of_rgb_colors(count)
    else:
        return 'Invalid color type. Use hexa or rgb.'

print(generate_colors('hexa', 3))  # ['#a3e12f', '#03ed55', '#eb3d2b']
print(generate_colors('hexa', 1))  # ['#b334ef']
print(generate_colors('rgb', 3))   # ['rgb(5,55,175)', 'rgb(50,105,100)', 'rgb(15,26,80)']
print(generate_colors('rgb', 1))   # ['rgb(33,79,176)']
