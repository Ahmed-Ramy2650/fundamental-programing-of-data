def rev(text):
    x = ""
    for i in range(len(text)-1, -1, -1):
        x += text[i]
    return x
def main():
    a = input("Enter the text to reverse: ").strip()
    print(rev(a))
if __name__ == "__main__":
    main()
