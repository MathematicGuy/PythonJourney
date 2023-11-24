import random

acc = int(input("Enter n: "))
def estimate_pi(n):
    num_points_circle = 0
    num_points_total = 0

    for dots in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        random_point = x ** 2 + y ** 2   #  r: distance of circle radius

        if random_point <= 1:
            num_points_circle += 1
        num_points_total += 1

    pi = (4*num_points_circle)/num_points_total
    print(pi)


estimate_pi(acc)
