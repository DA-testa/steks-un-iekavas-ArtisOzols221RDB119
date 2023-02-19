from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text2):
    stack = []
    for i, next in enumerate(text2):
        if next in "([{":
            stack.append(Bracket(next,i))

        elif next in ")]}":
            stack.append(Bracket(next,i))
            if are_matching(stack[-1].char,next) == False or len(stack)==0:
                stack.pop()
                return i+1
            else: stack.pop()

    if len(stack)==0:
        return "Success"
    else:
         return (stack[-1])

def main():
    text = input()
    if text[0]=="I":
        text2=input()
        mismatch=find_mismatch(text2)
        print(mismatch)

if __name__ == "__main__":
    main()
