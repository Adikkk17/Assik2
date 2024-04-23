
def read_input():
    n = int(input())
    add_input = []
    for i in range(n):
        addinput = list(map(int, input().split()[1:]))
        add_input.append(addinput)
    return add_input
def process_query(add_input):
    query = int(input())
    for i in range(query):
        x, y = map(int,input().split())
        if x >=1 and x <= len(add_input) and y>= 1 and y<=len(add_input[x-1]):
            print(add_input[x-1][y-1], " ")
        else:
            print("ERROR!")
def main():
    input_arr = read_input()
    process_query(input_arr)
if __name__ == "__main__":
    main()