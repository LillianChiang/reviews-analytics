data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 100000 == 0:
            print (len(data))

print('there are total:', len(data), 'records')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print('The average length of records is:', sum_len/len(data))
