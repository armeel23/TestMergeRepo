# Matt Popovich
# CMPSC 443 - Lab 01
# 1-21-16


# provide a list of imported modules here
import urllib2
import datetime
import operator

def list_2_dict(my_list):
    """
        This function taks as input a list of 2-tuples and and
        convert the list to a dictionary. The formart of the list
        is: [(k1, v1), (k2, v2), (k3, v3)] and the output is
        {k1:v1, k2:v2, k3:v3}
        For example, a test case would be:
        [(11, 'David'), (101, 'John'), (32, 'Lisa'), (55, 'Chris')]
    """
    if (my_list.startswith('[') & my_list.endswith(']')):
        my_list = my_list[1:-1]     # Remove first and last character
    else:
        return 'Invalid input, no leading "[" or trailing "]"'

    my_dict = '{'               # Add starting curly bracket

    while (len(my_list) > 5):

        start = my_list.index('(')
        end = my_list.index(')')
        tuple = my_list[start+1:end]    # Get tuple
        comma = tuple.index(',')
        first = tuple[0:comma]      # Get first variable of tuple
        second = tuple[comma+2:]    # Get second variable of tuple
        my_dict += first + ':' + second + ', '
        my_list = my_list[end+3:]   # Remove variables added to dictionary from list

    my_dict = my_dict[0:-2]     # Remove last comma
    my_dict += '}'              # Add ending curly bracket

    return  my_dict


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
    elif (n == 1):
        num = 1
    else:
        num = fib_rec(n-1) + fib_rec(n-2)

    return num


def fib_loop(n):
    """
    Write a iterative function to find the nth Fibonacci number
    0, 1, 1, 2, 3, 5 ...
    """
    num = 0
    if (n <= 0):
        num = 0
    elif (n == 1):
        num = 1
    else:
        a = 0
        b = 1
        for x in range(1,n):
            num = a + b
            a = b
            b = num
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
    dict = {}
    input = open(in_file, 'r')
    line = input.readline()                     # Read headers of .csv file
    for line in input:
        lastComma = line.rfind(',')
        target = line[lastComma+1:].strip()     # Remove whitespace from target
        if target.startswith('"') and target.endswith('"'):
            target = target[1:-1]               # Remove double quotes from target if present
        if (dict.has_key(target)):
            dict[target] = dict[target] + 1     # Increment target value if target is present
        else:
            dict[target] = 1                    # Add target to dictionary
    input.close()
                                                # Sort dictionary and make into list
    sortedDict = sorted(dict.items(), key=operator.itemgetter(0))

    output = open(out_file, 'w')

    for i, value in enumerate(sortedDict):      # Write all list values to file
        key = value[0]
        amount = value[1]
        output.write(key + ' - ')
        if (amount == 1):
            output.write(str(amount) + ' time\n')
        else:
            output.write(str(amount) + ' times\n')

    output.close()

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
    html = urllib2.urlopen(url).read()

    format = "%Y_%m_%d_%H_%M_%S"
    currentTime = datetime.datetime.now()
    filename = url[url.index('.')+1:]                   # Strip "http://www." from url
    filename = filename[0:filename.index('.')] + '-'    # Strip ".com/xxx/xxx///" from url
    filename += currentTime.strftime(format) + '.html'  # Add formatted time to filename
    
    f = open(filename, 'w')
    f.write(html)                                       # Write the html of the url to the file
    f.close()
    return filename


def test_list_2_dict():
	# please provide your test cases, as well as the output
    """ Output:
    Testing list_2_dict():
        list_2_dict("[(11, 'David'), (101, 'John'), (32, 'Lisa'), (55, 'Chris')]")
        = {11:'David', 101:'John', 32:'Lisa', 55:'Chris'} y
    """
    
    print "Testing list_2_dict():"
    print "\tlist_2_dict(\"[(11, 'David'), (101, 'John'), (32, 'Lisa'), (55, 'Chris')]\")"
    
    dict = list_2_dict("[(11, 'David'), (101, 'John'), (32, 'Lisa'), (55, 'Chris')]")
    print "\t= " + dict,
    if (dict == "{11:'David', 101:'John', 32:'Lisa', 55:'Chris'}"):
        print u'\u2713'
    else:
        print "X"
        return

def test_fib_rec():
    # please provide your test cases, as well as the output
    """ Output: 
    Testing fib_rec():
        fib_rec(0) = 0 y
        fib_rec(1) = 1 y
        fib_rec(6) = 8 y
    """
    
    print "Testing fib_rec():"
    
    uut = fib_rec(0)
    print "\tfib_rec(0) = " + str(uut),
    if (uut == 0):
        print u'\u2713'
    else:
        print "X"
        return

    uut = fib_rec(1)
    print "\tfib_rec(1) = " + str(uut),
    if (uut == 1):
        print u'\u2713'
    else:
        print "X"
        return

    uut = fib_rec(6)
    print "\tfib_rec(6) = " + str(uut),
    if (uut == 8):
        print u'\u2713'
    else:
        print "X"
        return


def test_fib_loop():
    # please provide your test cases, as well as the output
    """ Output:
    Testing fib_loop():
        fib_loop(0) = 0 y
        fib_loop(1) = 1 y
        fib_loop(6) = 8 y
    """
    
    print "Testing fib_loop():"
    
    uut = fib_loop(0)
    print "\tfib_loop(0) = " + str(uut),
    if (uut == 0):
        print u'\u2713'
    else:
        print "X"
        return
    
    uut = fib_loop(1)
    print "\tfib_loop(1) = " + str(uut),
    if (uut == 1):
        print u'\u2713'
    else:
        print "X"
        return
    
    uut = fib_loop(6)
    print "\tfib_loop(6) = " + str(uut),
    if (uut == 8):
        print u'\u2713'
    else:
        print "X"
        return


def test_file_processing():
	# please provide your test cases
    # Writes "facebook" once and "apple" twice to a .csv file
    """ Output:
    Testing test_file_processing():
        Writing a .csv file to test with y
        Running file_processing("testcsv.csv", "testoutput.txt") y
        Reading "testoutput.txt" and verifying correctness y
    """
    
    print "Testing test_file_processing():"
    print "\tWriting a .csv file to test with",
    
    csv = open("testcsv.csv", 'w')      # Create .csv file to test with
    csv.write("1,1,1,1,1,1,1,1\n")
    csv.write("1,1,1,1,1,1,1,facebook\n")
    csv.write("1,1,1,1,1,1,1,apple\n")
    csv.write("1,1,1,1,1,1,1,apple\n")
    csv.close()
    
    print u'\u2713'
    print '\tRunning file_processing("testcsv.csv", "testoutput.txt")',

    file_processing("testcsv.csv", "testoutput.txt")
    print u'\u2713'

    print '\tReading "testoutput.txt" and verifying correctness',

    txt = open("testoutput.txt", 'r')
    line1 = txt.readline()
    line2 = txt.readline()
    line3 = txt.readline()
        
    if ((line1 == "apple - 2 times\n") & (line2 == "facebook - 1 time\n") & (line3 == "")):
        print u'\u2713'                 # Verify that all lines in file are correct
    else:
        print "X"
        return

    return

def test_dump_webpage():
	# please provide your test cases
    # Reads from the most plain webpage I could find: http://www.december.com/html/demo/hello.html
    """
    Testing test_dump_webpage():
        Running dump_webpage('http://www.december.com/html/demo/hello.html')  y
        Reading the output .html file and verifying correctness  y
    """
    
    print "Testing test_dump_webpage():"
    print "\tRunning dump_webpage('http://www.december.com/html/demo/hello.html') ",
    
    filename = dump_webpage('http://www.december.com/html/demo/hello.html')
    print u'\u2713'

    file = open(filename, 'rb')
    contents = file.read()
    file.close()
    
    print "\tReading the output .html file and verifying correctness ",

    if (contents == urllib2.urlopen('http://www.december.com/html/demo/hello.html').read()):
        print u'\u2713'                 # Verify file written is what we expected
        return
    else:
        print "X"
        return


#############################
if __name__ == '__main__':
    test_list_2_dict()
    test_fib_loop()
    test_fib_rec()
    test_file_processing()
    test_dump_webpage()
#############################


""" Output:
Testing list_2_dict():
    list_2_dict("[(11, 'David'), (101, 'John'), (32, 'Lisa'), (55, 'Chris')]")
    = {11:'David', 101:'John', 32:'Lisa', 55:'Chris'} y
Testing fib_loop():
    fib_loop(0) = 0 y
    fib_loop(1) = 1 y
    fib_loop(6) = 8 y
Testing fib_rec():
    fib_rec(0) = 0 y
    fib_rec(1) = 1 y
    fib_rec(6) = 8 y
Testing test_file_processing():
    Writing a .csv file to test with y
    Running file_processing("testcsv.csv", "testoutput.txt") y
    Reading "testoutput.txt" and verifying correctness y
Testing test_dump_webpage():
    Running dump_webpage('http://www.december.com/html/demo/hello.html')  y
    Reading the output .html file and verifying correctness  y

"""