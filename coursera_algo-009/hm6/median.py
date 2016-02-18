from heapq import heappush, heappop

test_files = ["Median.txt"]

#test_files = ["test_Q2_01.txt", "test_Q2_02.txt"]


for filename in test_files:
    with open(filename, "r") as f:
        count = 0
        h_low = []
        h_high = []
        for line in f:
            i = int(line)
            len_low = len(h_low)
            len_high = len(h_high)

            if len_low == 0:
                m = i
                heappush(h_low, -i)
            elif len_high == 0:
                l = -(heappop(h_low))
                if l < i:
                    m = l
                    heappush(h_low, -l)
                    heappush(h_high, i)
                else:
                    m = i
                    heappush(h_low, -i)
                    heappush(h_high, l)
            else:
                l = -(heappop(h_low))
                h = heappop(h_high)

                a = sorted([l,h,i])

                if len_low > len_high:
                    heappush(h_low, -(a[0]))
                    heappush(h_high, a[1])
                    heappush(h_high, a[2])
                else:
                    heappush(h_low, -(a[0]))
                    heappush(h_low, -(a[1]))
                    heappush(h_high, a[2])

                low = heappop(h_low)
                m = -low
                heappush(h_low, low)

            #print m
            #print h_low
            #print h_high
            count = count + m

        print "Result: " + str(count)



