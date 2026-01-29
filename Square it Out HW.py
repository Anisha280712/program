def filter_square_values(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]

    print("All squares:", squares)
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)

filter_square_values(1, 10)
