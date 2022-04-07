milesPerYear = 14032
mPG = 126
galtoKWH = 33.7
gallonsUsed = milesPerYear // mPG
print(gallonsUsed)

costOR = 0.1116
totalCostOR = gallonsUsed * costOR * galtoKWH
print(totalCostOR)

costCA = 0.30
totalCostCA = gallonsUsed * costCA * galtoKWH
print(totalCostCA)