import SurvivalModelClasses as Cls




MORTALITY_PROB = 0.5    # annual probability of mortality
TIME_STEPS = 100        # simulation length
REAL_POP_SIZE = 573     # size of the real cohort to make the projections for
NUM_SIM_COHORTS = 1000   # number of simulated cohorts used for making projections
ALPHA = 0.05            # significance level

# calculating prediction interval for mean survival time
# create multiple cohorts
multiCohort = Cls.MultiCohort(
    ids=range(NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    pop_sizes=[REAL_POP_SIZE] * NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    mortality_probs=[MORTALITY_PROB]*NUM_SIM_COHORTS  # [p, p, ....]
)
# simulate all cohorts
multiCohort.simulate(TIME_STEPS)

Clinical_value = 0
for value in multiCohort._meanSurvivalTimes:
    if value > (400/573):
        Clinical_value += 1

prob_clin_trial_occurs=Clinical_value/1000

print('The likelihood the trial reports more than 400 of '
      '573 patients survive at the end of 5 years is',
      prob_clin_trial_occurs)
