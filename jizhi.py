try:
    f = open(r"test.py", "a")
    strs = "gaoqi"
    f.write(strs)
except BaseException as e:
    print(e)
finally:
    f.close()