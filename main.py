# def main():
#     print("Hello from algorithms!")


# if __name__ == "__main__":
#     main()

def some_func(s):
  r = ""
  for i in s[::-1]:
    r += i
  return r

print(some_func("yeah"))
