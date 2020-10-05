def multiply_string(n, message):
    for i in range(0, n):
        message = message * n
        return(message)

if __name__ == '__main__':
    print(multiply_string(4, "Mike"))



