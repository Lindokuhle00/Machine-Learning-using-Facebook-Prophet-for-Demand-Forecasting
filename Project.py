
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Calculate capability metrics
USL = 1.5
LSL = None  # not provided

# Given process parameters
mean = 2.4
std_within = 1.60698
std_overall = 1.4704
USL = 1.5
sample_size = 30

np.random.seed(42)
data = np.random.normal(mean, std_overall, sample_size)

# Cpk for upper spec limit only (since LSL is missing)
Cpu = (USL - mean) / (3 * std_within)
Z_usl = (USL - mean) / std_within
Zbench = Z_usl  # approximation since one-sided

# PPM (expected defects above USL)
PPM_usl = (1 - stats.norm.cdf(Z_usl)) * 1_000_000

# Recreate the plot with metrics annotated
plt.figure(figsize=(9,6))
count, bins, ignored = plt.hist(data, bins=8, density=True, color='lightgrey', edgecolor='black')

x = np.linspace(min(bins), max(bins), 100)
plt.plot(x, stats.norm.pdf(x, mean, std_within), 'r-', linewidth=2, label='Within')
plt.plot(x, stats.norm.pdf(x, mean, std_overall), 'k--', linewidth=2, label='Overall')
plt.axvline(USL, color='red', linestyle='--', linewidth=2)
plt.text(USL+0.05, 0.05, 'USL', color='red')

# Title and labels
plt.title('Process Capability of Time Stoppage', fontsize=14, weight='bold')
plt.xlabel('Time Stoppage')
plt.ylabel('Density')
plt.legend()

# Add text box for metrics
textstr = '\n'.join((
    f'Mean = {mean:.2f}',
    f'Std (Within) = {std_within:.3f}',
    f'Std (Overall) = {std_overall:.3f}',
    f'USL = {USL}',
    f'Z.USL = {Z_usl:.2f}',
    f'Z.Bench = {Zbench:.2f}',
    f'Cpk = {Cpu:.2f}',
    f'PPM > USL = {PPM_usl:,.0f}'
))


#sjdjdjdjkd
# Add an LSL value for a more complete table
LSL = 0.5

# Calculate Z values and capability indices
Z_usl = (USL - mean) / std_within
Z_lsl = (mean - LSL) / std_within
Zbench_within = min(Z_usl, Z_lsl)
Cpk = min((USL - mean), (mean - LSL)) / (3 * std_within)

Z_usl_overall = (USL - mean) / std_overall
Z_lsl_overall = (mean - LSL) / std_overall
Zbench_overall = min(Z_usl_overall, Z_lsl_overall)
Ppk = min((USL - mean), (mean - LSL)) / (3 * std_overall)

# Calculate PPM values
PPM_usl = (1 - stats.norm.cdf(Z_usl)) * 1_000_000
PPM_lsl = stats.norm.cdf(-Z_lsl) * 1_000_000
PPM_total = PPM_usl + PPM_lsl

# Plot histogram and curves
plt.xlim(min(bins), max(bins) + 1.5)  # Adds empty space on the right
plt.tight_layout(pad=5)


plt.hist(data, bins=8, density=True, color='lightgrey', edgecolor='black')
x = np.linspace(min(bins), max(bins), 100)
plt.plot(x, stats.norm.pdf(x, mean, std_within), 'r-', linewidth=2, label='Within')
plt.plot(x, stats.norm.pdf(x, mean, std_overall), 'k--', linewidth=2, label='Overall')

# Add spec limit lines
plt.axvline(USL, color='red', linestyle='--', linewidth=2)
plt.axvline(LSL, color='blue', linestyle='--', linewidth=2)
plt.text(USL+0.05, 0.05, 'USL', color='red')
plt.text(LSL-0.4, 0.05, 'LSL', color='blue')

# Title and labels
plt.title('Process Capability of Time Stoppage', fontsize=14, weight='bold')
plt.xlabel('Time Stoppage')
plt.ylabel('Density')
plt.legend()

# Text boxes for detailed metrics
text_within = (
    "Potential (Within) Capability\n"
    f"Z.Bench = {Zbench_within:.2f}\n"
    f"Z.LSL = {Z_lsl:.2f}\n"
    f"Z.USL = {Z_usl:.2f}\n"
    f"Cpk = {Cpk:.2f}"
)

text_overall = (
    "Overall Capability\n"
    f"Z.Bench = {Zbench_overall:.2f}\n"
    f"Z.LSL = {Z_lsl_overall:.2f}\n"
    f"Z.USL = {Z_usl_overall:.2f}\n"
    f"Ppk = {Ppk:.2f}"
)

# Combine both sections in one box (like original layout)
capability_text = text_within + "\n\n" + text_overall
plt.text(4.3, 0.29, capability_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))


# Observed performance (simulated values)
performance_text = (
    "Observed Performance\n"
    f"PPM < LSL = {PPM_lsl:,.2f}\n"
    f"PPM > USL = {PPM_usl:,.2f}\n"
    f"PPM Total = {PPM_total:,.2f}"
)

plt.text(4.3, 0.18, performance_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

#plt.text(6, 0.1, "text here")  # moves slightly left and up


plt.grid(False)
plt.show()



plt.text(5.2, 0.32, textstr, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))


plt.tight_layout(pad=3)

plt.grid(False)
plt.show()
