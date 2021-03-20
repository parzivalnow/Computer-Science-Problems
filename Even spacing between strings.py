### Even spacing between words with extra spaces at the end

def reorderSpaces(self, text: str) -> str:
        length = len(text)
        text = text.split()
        if len(text) == 1:
            return text[0] + (length-len(text[0])) * " "
        words = [len(x) for x in text]
        spaces, remainder = (length - sum(words))//(len(words)-1), (length - sum(words))%(len(words)-1)

        newStr = ""

        for i in range(len(text)):
            newStr += text[i]
            if i != (len(text)-1):
                newStr += " " * spaces
            else:
                newStr += " " * remainder

        return newStr
