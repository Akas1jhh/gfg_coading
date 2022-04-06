    def findSwapValues(self,a, n, b, m):
       a.sort()
       b.sort()
       suma = sum(a)
       sumb = sum(b)
       i=0
       j=0
       while (i<n and j<m):
           p = suma - a[i] + b[j]
           q = sumb - b[j] + a[i]
           if (p == q):
               return 1
           if (p > q):
               i+=1
           else:
               j+=1
       return -1