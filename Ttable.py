# generating transition tablr
def get_Ttable(data,K=3): # k is simply the number of chars we are considering can be any value (but let say 3)
    T = {}
    l = len(data)
    for i in range(l-K):
        X = data[i:i+K]
        Y = data[i+K]

        if T.get(X) is None:
            T[X] = {}
            T[X][Y] = 1
        else :
            if T[X].get(Y) is None:
                T[X][Y] = 1
            else :
                T[X][Y] += 1
    return T
def get_freq_probab(T):
    for kv in T.keys():
        s = sum(T[kv].values())
        for k in T[kv].keys():
            T[kv][k] = T[kv][k]/s
    return T
def text_sample(filepath):
    with open(filepath) as f:
        return f.read()
def Markoniv_model(text , k=3):
    T = get_Ttable(text , k)
    T = get_freq_probab(T)
    return T
import random
def next_char(context , T, k):
    context = context[-k:]
    if T.get(context) is None :
        return " "
    else :
        poss_chars = list(T.get(context).keys())
        poss_freq = list(T.get(context).values())
        return random.choices(poss_chars,weights=poss_freq)[0]
def generate_Text(context , T , k  = 3, max_len = 100):
    context1 = context
    context2 = context[-k:]
    for i in range (max_len):
        next_pred = next_char(context2 , T , k=3)
        context1 += next_pred
        context2 = context1[-k:]
    return (context1)
text = text_sample("Textsample.txt")
T = get_Ttable(text)
T1 = get_freq_probab(T)
T2 = Markoniv_model(text)
a0 = generate_Text("congr" , T2 , 3 , 100 )
a = next_char("congrats every ream of me sp" , T2 , 3)
# print(T)
# print(get_freq_probab(T))
# print(text)
# print(T2)
print(a0)
# print(a)


    