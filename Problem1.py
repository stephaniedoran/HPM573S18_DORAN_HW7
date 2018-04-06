import SurvivalModelClasses as Cls

MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
SIM_POP_SIZE = 573     # population size of the simulated cohort
ALPHA = 0.05            # significance level

# create a cohort of patients
myCohort = Cls.Cohort(id=1, pop_size=SIM_POP_SIZE, mortality_prob=MORTALITY_PROB)

# simulate the cohort
cohortOutcome = myCohort.simulate(TIME_STEPS)

# percentage survived after 5 years

count_alive_after_5 = 0

for value in cohortOutcome.get_survival_times():
    if value > 5:
        count_alive_after_5 +=1

percent_alive=(count_alive_after_5/SIM_POP_SIZE)

print('The percentage of patients surviving after 5 years is', percent_alive*100, '%')
