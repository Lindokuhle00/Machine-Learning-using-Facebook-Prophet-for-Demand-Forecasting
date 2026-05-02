import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# ===== Process Data =====
LSL = 1.8
USL = 2.5
Cpl = 0.00
Cpu = 0.4103
Cpk = 0.000
mean = 1.8
Target = 4
std_within = 0.568622
std_overall = 0.664364
n = 30

# ===== Synthetic Data =====
np.random.seed(42)
data = np.random.normal(mean, std_overall, n)

# ===== Plot =====
plt.figure(figsize=(10,6))
plt.hist(data, bins=8, density=True, color='lightgrey', edgecolor='black')

# Normal curve
x = np.linspace(mean - 3*std_overall, mean + 3*std_overall, 100)
plt.plot(x, stats.norm.pdf(x, mean, std_within), 'r-', linewidth=2, label='Within')

# LSL line
plt.axvline(LSL, color='blue', linestyle='--', linewidth=2)
plt.text(LSL - 0.2, 0.03, 'LSL', color='blue', fontsize=9)

# Labels
plt.title('Process Capability of Time Stoppage', fontsize=12, weight='bold')
plt.xlabel('Time Stoppage')
plt.ylabel('Density')
plt.legend()

# ===== Text Sections =====

# 1️⃣ Process Data
process_text = (
    f"Process Data\n"
    f"LSL = {LSL}\n"
    f"Target = {Target}\n"
    f"USL = {USL}\n"
    f"Sample Mean = {mean}\n"
    f"Sample N = {n}\n"
    f"StDev (Within) = {std_within:.6f}\n"
    f"StDev (Overall) = {std_overall:.6f}"
)

#kkkk
plt.text(mean + 3.65*std_overall, 0.1, process_text, fontsize=9,
         bbox=dict(facecolor='white', alpha=0.8))

# 2️⃣ Capability Results
capability_text = (
    "Potential (Within) Capability\n"
    "Cp = {Cp}  Cpl = 0.00  Cpu = {Cpu}  Cpk = 0.00\n\n"
    "Overall Capability\n"
    "Pp = *  Ppl = 0.00  Ppu = *  Ppk = 0.00  Cpm = *"
)
plt.text(mean + 2.2*std_overall, -0.40, capability_text, fontsize=8.5,
         bbox=dict(facecolor='white', alpha=0.8))

# 3️⃣ Observed Performance
ppm_text = (
    "Observed Performance\n"
    "PPM < LSL = 266,666.67\n"
    "PPM > USL = *\n"
    "PPM Total = 266,666.67\n\n"
    "Exp. Within Performance\n"
    "PPM < LSL = 500,000.00\n"
    "PPM > USL = *\n"
    "PPM Total = 500,000.00\n\n"
    "Exp. Overall Performance\n"
    "PPM < LSL = 500,000.00\n"
    "PPM > USL = *\n"
    "PPM Total = 500,000.00"
)
plt.text(mean + 3.7*std_overall, 0.6, ppm_text, fontsize=8.5,
         bbox=dict(facecolor='white', alpha=0.8))

# ===== Adjust layout =====
plt.xlim(mean - 3*std_overall, mean + 3.5*std_overall)
plt.tight_layout(pad=2)
plt.show()
