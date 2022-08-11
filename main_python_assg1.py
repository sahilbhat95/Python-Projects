import numpy as np
# Task 1------------------------------------------------------------
def mark_calculated(mid_mark1, mid_mark2, final_mark):
  '''--------------------------------------
  Calculate the total mark provide that
  mid_mark1 counts 20%
  mid_mark2 counts 30%
  final_mark counts 50%
  -----------------------------------------
  Keyword Arguments:
  mid_mark1   -- A non-negative number in [0, 100], e.g., 50 or 60.5
  mid_mark2   -- A non-negative number in [0, 100], e.g., 50 or 60.5
  final_mark -- A non-negative number in [0, 100], e.g., 50 or 60.5
  -----------------------------------------
  Returns:
  total_mark -- A number, e.g., 50 or 60.5  
  If the inputs are not allowed (e.g. negative numbers) then return 'Inputs are not allowed' 
  -----------------------------------------'''
  total_mark=0 
  # add code here to calculate the total_mark
  if (mid_mark1<0 or mid_mark2<0 or final_mark<0 or mid_mark1>100 or mid_mark2>100 or final_mark>100):
    return ('Inputs are not allowed')
  else:
   total_mark= 0.2*mid_mark1 + 0.3*mid_mark2 + 0.5*final_mark
   return  total_mark # Do NOT do changes here

# Task 2------------------------------------------------------------
def mark_result(total_mark):
  '''------------------------------------
  Mark the grade based on the total_mark
  result = "Distinction" if total_mark in [70, 100]
  result = "Merit" if total_mark in [60, 70)
  result = "Pass" if total_mark in [50, 60)
  result = "Fail" if total_mark in [0, 50)
  ---------------------------------------
  Keyword Arguments:
  total_mark -- A non-negative number in [0, 100] e.g. 50 or 60.5
  ---------------------------------------
  Returns:
  result -- A text string, e.g., 'Distinction' or 'Pass'  
  If the inputs are not allowed (e.g negative numbers) then return 'Inputs are not allowed' 
  ---------------------------------------'''
  result = 'None' # Do NOT do changes here
  #total_mark= mark_calculated(mid_mark1, mid_mark2, final_mark)
  if (total_mark>= 70 and total_mark <=100):
    result= 'Distinction'
    #print (result)
  elif (total_mark>= 60 and total_mark<70):
    result= 'Merit'
    #print (result)
  elif (total_mark>= 50 and total_mark<60):
    result= 'Pass'
    #print (result)
  elif (total_mark>= 0 and total_mark<50):
     result= 'Fail'
    #print (result)
  elif (total_mark<0 or total_mark>100):
     result= 'Inputs are not allowed'
  return result # Do NOT do changes here

# Task 3------------------------------------------------------------
def summary_statitics(file_name):
  '''--------------------------------------------------------------
  Return the following info:
  1) The indices of the dates with the highest and positive lowest number (i.e., not zeros) of new confirmed cases. 
  (Note: if there is more than one highest or one positive lowest number, you should print out all the indices. The printed indices should be integers between 0 and 259.)
  2) The mean and standard deviation of the data (cases_mean, cases_std)
  3) The indices of the top 5% of dates of new cases and the total new cases in this group
  -----------------------------------------------------------------
  Keyword Arguments:
  file_name -- A text string, the file name, e.g.,'student_mark.csv' 
  -----------------------------------------------------------------
  Returns:
  max_ind   -- A list with integer entries, e.g, [0] or [0,2,100]
  min_ind   -- A list with integer entries, e.g, [0] or [0,2,100]
  cases_mean    -- A floating number, mean of the cases
  cases_std     -- A floating number, standard deviation of the cases
  top5 --  A list with integer entries, e.g, [0] or [0,2,100]
  total_top5 -- A positive number, sum of all cases in top 5% of days
  ------------------------------------------------------------------
  Note: Returns must follow the given formats/data type. 
  Otherwise your results will be marked wrong.
  ------------------------------------------------------------------''' 

  max_ind = [] # Do NOT do changes here
  min_ind = [] # Do NOT do changes here
  cases_mean  = 0 # Do NOT do changes here
  cases_std   = 0 # Do NOT do changes here
  top5  = [] # Do NOT do changes here
  total_top5 = 0 # Do NOT do changes here

  # add code here to calculate max_ind, min_ind, cases_mean, cases_std, top5, total_top5]

  covid_data= np.genfromtxt(file_name, skip_header= 1, delimiter= ',', dtype= np.int64)
  max_ind= highest_case_index (covid_data,max_ind)
  min_ind= second_lowest_case_index (covid_data,min_ind)
  cases_mean,cases_std= cal (covid_data, cases_mean, cases_std)
  top5, total_top5= top_percentile (covid_data, top5, total_top5)
  return max_ind, min_ind, cases_mean, cases_std, top5, total_top5 # Do NOT do changes here

def highest_case_index (covid_data,max_ind): # function to calculate index of data with highest cases
  max_case= covid_data.max()
  for i in range (259):
    if (covid_data[i]==max_case):
      max_ind.append (i)
  return max_ind

def second_lowest_case_index (covid_data,min_ind): # function to calculate index of data with second lowest cases 
  sort_arr=sorted(covid_data) # to arrange data in ascending order
  for i in range (260):
    if (sort_arr[i]!=0): # to find data less than zero, as data is already in ascending order
      lowest_num= sort_arr[i] 
      break
  for j in range (260):
    if (covid_data[j]==lowest_num):
      min_ind.append(j)
  return min_ind
  
def cal (covid_data, cases_mean, cases_std):
  cases_mean=covid_data.mean()
  cases_std=covid_data.std()
  return cases_mean, cases_std

def top_percentile (covid_data, top5, total_top5):
  top_per= np.percentile(covid_data,95)
  per_5=(np.where (covid_data >= top_per))
  top5= per_5[0]
  for i in top5:
    total_top5= total_top5+covid_data[i]
  return top5, total_top5

# Do NOT do changes the code below
def test():

    file_name = './London_COVID19_new_cases_by_specimen_date.csv'

    print('---------------- Task 1 ------------------------')
    mid_mark1 = 50
    mid_mark2 = 60
    final_mark = 70
    print(mark_calculated(mid_mark1, mid_mark2,final_mark))

    print('---------------- Task 2 ------------------------')
    print(mark_result(75))

    print('---------------- Task 3 ------------------------')
    max_ind, min_ind, cases_mean, cases_std, top5, total_top5 = summary_statitics(file_name)
    print('\tIndices of the highest number:         {0}'.format(max_ind))
    print('\tIndices of the lowest non-zero number: {0}'.format(min_ind))
    print(cases_mean, cases_std)
    print(top5)
    print(total_top5)
    
    
def main():
    test()
    #total_mark= mark_calculated (70,74,75)
    #mark_result(total_mark)


if __name__ == "__main__":
    main()

