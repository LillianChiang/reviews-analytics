data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 100000 == 0:
            print (len(data))
print('There are total:', len(data), 'records')


sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('The average length of records is:', sum_len/len(data))


new  = []
for d in data:
        if len(d) < 100:
            new.append(d)
print('There are ', len(new), 'records less than 100 words')
print('--------------------------------------------------------------------------')
print(new[0])
print('--------------------------------------------------------------------------')
print(new[1])


#good = [d for d in data if 'good' in d]
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('There are ',len(good), 'records mentioned good')
print(good[0])



