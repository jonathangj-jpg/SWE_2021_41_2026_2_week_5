def isHappy(n):
  list1=[]

  while 1:
    if n==1:
      return True
    list1.append(n)
    digits = [int(digit) for digit in str(n)]
    n = sum(digit ** 2 for digit in digits)
    if n in list1:
      return False


if __name__ == "__main__":
  sample0_output = isHappy(19)
  sample1_output = isHappy(2)
  with open("/app/bind_mount/output.txt", "w") as f:
    f.write(f"19: {sample0_output}\n")
    f.write(f"2: {sample1_output}\n")
  print("Results saved to /app/bind_mount/output.txt")