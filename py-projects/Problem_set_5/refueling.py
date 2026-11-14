def main():
    raw_input = input("fraction: ")
    print(gauge(convert(raw_input)))

def convert(xy):
    result = xy.split("/")
    result_x = int(result[0])
    result_y = int(result[1])
    if result_x > result_y and result_y > 0:
       raise TypeError# "hello" / result_y
    return result_x / result_y

def gauge(s):
    s_percentage = s * 100
    if s_percentage > 98: 
        return "F"
    elif s_percentage < 2:
        return 'E' 
    else: return (str(int(s_percentage)) + "%")   

if __name__ == "__main__":
    main()