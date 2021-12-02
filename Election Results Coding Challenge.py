import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

# Total voted for Ceballos
total_ceballos = sum([1 for response in survey_responses if response == 'Ceballos'])
print(total_ceballos)

# length of the survey
survey_length = float(len(survey_responses))
# print(survey_length)

#percentage of voters who voted Ceballos
percentage_ceballos = total_ceballos / survey_length
# print(percentage_ceballos)

# binomial distribution
possible_surveys = np.random.binomial(survey_length, .54, size=10000) / survey_length

#plotting of the histogram
# plt.hist(possible_surveys, range=(0, 1), bins=20)
# plt.show()


# percentage of surveys less than 50%
possible_surveys_length = float(len(possible_surveys))

incorrect_predictions = len(possible_surveys[possible_surveys < .5])

ceballos_loss_surveys = incorrect_predictions / possible_surveys_length
# print(ceballos_loss_surveys)

# new distribution with 7000 people sample size
large_survey_length = float(7000)
large_survey = np.random.binomial(large_survey_length, .54, size=10000) / large_survey_length

# plt.close()
plt.hist(possible_surveys, range=(0, 1), bins=20)
plt.hist(large_survey, alpha=0.5, range=(0, 1), bins=20)
plt.show()

# new outcome of ceballos losing 
incorrect_predictions = len(large_survey[large_survey < .5])
ceballos_lost_new = incorrect_predictions / large_survey_length
print(ceballos_lost_new)