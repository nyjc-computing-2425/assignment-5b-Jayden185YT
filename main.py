# Part 1
def read_csv(filename):
    # Type your code below
    "Read CSV data stored in filename"
    file = open(filename, "r")
    header = file.readline().strip().split(',')
    data = []
    for line in file:
      field = line.strip().split(',')
      row = [int(field[0]), field[1], field[2],       int(field[3])]
      data.append(row)
    file.close()
    return header, data
    


# Part 2
def filter_gender(enrolment_by_age, sex):
    # Type your code below
    '''
    Function that returns a list of records where the         value in the "sex" column matches string sex
    '''
    result = []
    for line in enrolment_by_age:
      student = []
      if line[2] == sex:
        student.append(int(line[0]))
        student.append(line[1])
        student.append(int(line[3]))
        result.append(student)
    return result


# Part 3
def sum_by_year(enrolment):
    '''
    Function that sums up the total enrolment 
    of that year
    '''
    result = []
    year = 1984
    curr_year = [year, 0]
    for line in enrolment:
      if line[0] > year:
        year = line[0]
        result.append(curr_year)
        curr_year = [year, 0]
      curr_year[1] += line[2]
    result.append(curr_year)
    return result

# Part 4
def write_csv(filename, header, data):
    # Type your code below
    '''
    Function that will write header and data to filename
    and returns the number of lines written
    '''
    file = open(filename, "w")
    file.write(','.join(header) + '\n')
    lines = 1
    for line in data:
      file.write(','.join(map(str, line)) + '\n')
      lines += 1
    return lines
    
# TESTING
# You can write code below to call the above functions
# and test the output
