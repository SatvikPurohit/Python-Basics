def div_sub(func):
    def decorator(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return decorator


# a > b so that not no fraction
div = div_sub(lambda a, b: a//b)
# a > b so that not no negative
sub = div_sub(lambda a, b: a - b)

print("Divide ", div(2, 8))
print("Substract ", sub(2, 8))
