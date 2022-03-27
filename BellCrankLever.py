# **************************************************************************************************************************************************************************************************** #
# ********************************************************************** 9.	To verify the law of moments using Bell crank lever  ********************************************************************* #
# **************************************************************************************************************************************************************************************************** #
# -@ AmiLab


'''
Note-
    - **DATA VALIDATION EXCLUDED FOR BEING CHECKED AT THE TIME OF DATA INPUT**
    - All Testings have been logged into the terminal for future debuggings.
    - All the Weights, Tensions and Lengths are to be provided in their respective unit systems, with the same units.
'''


# ********************************************************************** Argument / Variable Declaration (for Testing purposes) ********************************************************************** #



n = 5                                                                          # The Total Number of Observations been performed
W = [10, 20, 30, 40, 50]                                                       # The Loads to be hunged on the Lever
d = {1: [18, 18, 18, 18, 18], 2: [18, 19, 18, 20, 16]}                         # The Length of the Arms on the 2 ends, (i.e., d1, d2)
S = {1: [4, 8, 12, 16, 20], 2: [24, 33, 42, 51, 68]}                           # The Initial (before hanging the Weights) and Final (after hanging the additional Weights) Spring Balance Readings



# **************************************************************************************** Section ends here **************************************************************************************** #


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #



# ********************************************************************* Verification the law of moments using Bell crank lever  ********************************************************************* #



def slNo(n):                                                        # For Generating the Serial Numbers for the Observations
    return list(range(1, n + 1))

# Testing-
SlNo = slNo(n)
print('Observation Numbers (N) : ', SlNo)


def calTensionInSpringBal(S, n):                                     # For Calculating the Tensions in the Spring balance corresponding to every Observation with Load been Applied
    global A, B
    A, B = list(S.keys())[0], list(S.keys())[1]
    return [S[B][i] - S[A][i] for i in range(n)]

# Testing-
T = calTensionInSpringBal(S, n)
print('Tensions in the Spring Balance (T) : ', T)


def calMomentsOfSpringBalEnds(W, d, n):                                # For Calculating the Momemts of Forces (Weights applied and Tension generated by them) at both the Ends of the Spring Balance, caused due to the Weights hunged and the Tension Gnerated by them
    return {A : [W[i] * d[A][i] for i in range(n)], B : [W[i] * d[B][i] for i in range(n)]}

# Testing-
M = calMomentsOfSpringBalEnds(W, d, n)
print('Moments of Forces on the 2 sides of the Lever (M) : ', M)


def calPercentageError(M, n):                                           # For Calculating the Percentage Errors corresponding to each Observation made
    return [((M[B][i] - M[A][i]) * 100) / M[B][i] for i in range(n)]

# Testing-
percentage_err = calPercentageError(M, n)
print('Percentage Errors encountered during each Observation made :',end = ' [ ')
print(*[str(i) + '%' for  i in percentage_err], sep = ', ', end = ' ]\n')


def avgPercentageError(percentage_err, n):                              # For Calculating the Average of all the Percentage Errors Generated during each Observation
    return sum(percentage_err) / n

# Testing-
avg_percentage_err = avgPercentageError(percentage_err, n)
print(f'The Average Percentage Error = {avg_percentage_err} %')


# ********************************************************************************* Section ends here *********************************************************************************************** #


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #




