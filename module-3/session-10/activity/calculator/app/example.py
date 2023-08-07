import operations as c


def example(num_1, num_2):
    res_sum = c.sum(num_1, num_2)
    print(f"res_sum: {res_sum}")

    res_substract = c.substract(num_1, num_2)
    print(f"res_substract: {res_substract}")

    res_divide = c.divide(num_1, num_2)
    print(f"res_divide: {res_divide}")

    res_multiply = c.multiply(num_1, num_2)
    print(f"res_multiply: {res_multiply}")


if __name__ == "__main__":
    example(1, 0.5)
