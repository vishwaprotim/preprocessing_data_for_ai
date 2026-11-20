# Central Tendency
# Mean - Mathematical average
# Median - Middlemost element of a sorted dataset. If size is even we take the mean
# Mode - Most frequently occurring element

import numpy as np;

study_hours = [10,8,5,7,6,12,4]
print(f"Mean: {np.mean(study_hours):.2f}")
print(f"Mode: {np.median(study_hours):.2f}")
print(f"Variance: {np.var(study_hours):.2f}")
print(f"Standard Deviation: {np.std(study_hours):.2f}")