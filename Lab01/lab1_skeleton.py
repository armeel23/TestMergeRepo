# provide a list of imported modules here


def list_2_dict(my_list):
	"""
	This function taks as input a list of 2-tuples and and 
	convert the list to a dictionary. The formart of the list
	is: [(k1, v1), (k2, v2), (k3, v3)] and the output is
	{k1:v1, k2:v2, k3:v3}
	For example, a test case would be:
	[(11, 'David'), (101, 'John'), (32, 'Lisa'), (55, 'Chris')] 
	"""
	return my_dict


def fib_rec(n):
	"""
	Write a recursive function to find the nth Fibonacci number
	0, 1, 1, 2, 3, 5 ...
	The recursive definition of the Fib number series is:
	f(i) = f(i-1) + f(i-2)
	f(0) = 0
	f(1) = 1
	"""
    if (n <= 0):
        num = 0
    else if (n == 1):
        num = 1
    else:
        num = fib_rec(n-1) + fib_rec(n-2)
        
	return num


def fib_loop(n):
	"""
	Write a iterative function to find the nth Fibonacci number
	0, 1, 1, 2, 3, 5 ...
	"""
	return num


def file_processing(in_file, out_file):
	"""
	This function reads a file named 'in_file.csv'. Each 
	entry contains the info about an identifed phishing site.
	Most of them have been taken down since all of these sites 
	are found nearly a month ago. For each entry, the last column 
	shows the target. As you can see, most targets are 'other'.
	Your task is: for each target (company brand), count how many 
	times it is attacked; output your result in a file named by
	the 2nd parameter of the function. Your output file may look
	like this:
	-------------------------
	'other' - xxx times
	'paypal' - yyy times
	'facebook' - zzz times
	...
	-------------------------
	Please sort the targets in decending order based on the count.
	check this out regarding sorting a dict by value
	http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
	"""
	return

def dump_webpage(url):
	"""
	Given an url, write a function to dump the html content, and
	save it in the same directory of your python script. The name
	of the saved html file should include the current time stamp.
	hint:
	1. use python's built-in library 'urllib2' to make a http request
	check out the first answer of this:
	http://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
	2. The format of your timestamp: YYYY_MM_DD_HH_MM_SS
	For example, 2015_01_15_09_51_20 is a valid timestamp
	Please use the 'datetime' python module to get current time and the 'strftime'
	method to format your time.	
	"""
	return


def test_list_2_dict():
	# please provide your test cases, as well as the output
	pass


def test_fib_rec():
	# please provide your test cases, as well as the output
	pass


def test_fib_loop():
	# please provide your test cases, as well as the output
	pass


def test_file_processing():
	# please provide your test cases
	pass

def test_dump_webpage():
	# please provide your test cases
	pass

if __name__ == '__main__':
	# test_list_2_dict()
	# test_fib_loop()
	# test_fib_rec()
	# test_file_processing()
	# test_dump_webpage()
	pass