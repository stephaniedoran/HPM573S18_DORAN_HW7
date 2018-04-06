import scipy.stats as stat


SIM_POP_SIZE = 1000       # population size of simulated cohorts
TIME_STEPS = 1000        # length of simulation
ALPHA = 0.05             # significance level for calculating confidence intervals
NUM_SIM_COHORTS = 500   # number of simulated cohorts used to calculate prediction intervals

# details of a clinical study estimating the mean survival time
OBS_N = 1146        # number of patients involved in the study
OBS_MEAN = 6.9    # estimated mean survival time
OBS_HL = 1.5      # half-length
OBS_ALPHA = 0.05   # significance level
# the standard deviation of the mean survival time reported in the clinical study
# assumes that the reported confidence interval in this study is a t-confidence interval
OBS_STDEV = OBS_HL / stat.t.ppf(1 - OBS_ALPHA / 2, OBS_N-1)

# how to sample the posterior distribution of mortality probability
# minimum, maximum and the number of samples for the mortality probablity
POST_L, POST_U, POST_N = 0, 1, 1000

import CalibrationClasses as Cls


# initialize a calibrated model
calibrated_model = Cls.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model.simulate(NUM_SIM_COHORTS, SIM_POP_SIZE, TIME_STEPS)


# report mean and projection interval
print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(ALPHA, deci=4))
