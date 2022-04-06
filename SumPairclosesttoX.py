def sumClosest(self, arr, x):
  MAX_VAL = 1000000000
	res_l, res_r = 0, 0
	l, r, diff = 0, n-1, MAX_VAL

	while r > l:
    if abs(arr[l] + arr[r] - x) < diff:
			res_l = l
			res_r = r
			diff = abs(arr[l] + arr[r] - x)

		  if arr[l] + arr[r] > x:
		    # If this pair has more sum, move to
		    # smaller values.
			    r -= 1
		    else:
		    # Move to larger values
			      l += 1
		
	    return arr[res_l], arr[res_r]