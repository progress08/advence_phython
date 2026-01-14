import string

def analyze_text(n, m):
    f = open(n)
    data = f.readlines()
    f.close()
    dic = {}
    count = 0
    for i in data:
        temp = i.lower()
        for p in string.punctuation:
            temp = temp.replace(p,"")
        arr = temp.split()
        count+=len(arr)
        for j in arr:
            if j not in dic:
                dic[j]=1
            else:
                dic[j]+=1
    
    w = open(m, "w")
    w.write("Total number of lines: "+str(len(data))+"\n")
    w.write("Total number of words: "+str(count)+"\n")
    w.write("Word Frequencies:\n")
    for k in dic:
        w.write(k+": "+str(dic[k])+"\n")
    w.close()
    print("Analysis complete. Results saved to "+m)

if __name__ == "__main__":
    analyze_text("text.txt", "analysis.txt")
