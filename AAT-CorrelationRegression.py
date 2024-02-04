
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

# Physics scores
physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
# History scores
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

# Calculate the mean of physics scores
mean_physics = sum(physics_scores) / len(physics_scores)
# Calculate the mean of history scores
mean_history = sum(history_scores) / len(history_scores)

# Calculate the numerator of the Pearson correlation coefficient
numerator = sum((x - mean_physics) * (y - mean_history) for x, y in zip(physics_scores, history_scores))

# Calculate the denominator of the Pearson correlation coefficient
denominator_physics = math.sqrt(sum((x - mean_physics) ** 2 for x in physics_scores))
denominator_history = math.sqrt(sum((y - mean_history) ** 2 for y in history_scores))

# Calculate the Pearson correlation coefficient
correlation_coefficient = numerator / (denominator_physics * denominator_history)

# Print the Pearson correlation coefficient rounded to 3 decimal places
print("{:.3f}".format(correlation_coefficient))
