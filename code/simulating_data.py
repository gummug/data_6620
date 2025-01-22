import numpy as np
import pandas as pd
from scipy.special import expit
from sklearn.linear_model import LogisticRegression

np.random.seed(42)

# Updated parameter values
beta0 = -12.5  # Lowered to achieve class balance
beta1 = 0.3    # Race_White
beta2 = 0.3    # Age
beta3 = 0.3     # Gender_Male
beta4 = 0.1   # Undergrad
beta5 = 0.5   # Full-Time
beta6 = 0.3   # Program Score
beta7 = 0.5    # GPA
beta8 = 0.7     # Engagements
beta9 = 0.9    # Internships
beta10 = 0.3   # Industry Score
beta11 = -0.3   # From Utah

n = 2000

# Simulate programs and industries
program_effects = {
    'Accounting': 0.9, 'Business': 0.5, 'Business Administration': 0.4,
    'Data Analytics': 1.0, 'Economics': 0.6, 'Finance': 0.7,
    'Information Systems': 0.9, 'International Business': 0.3,
    'Management': 0.5, 'Marketing': 0.6
}
industry_effects = {
    'Healthcare & Social Assistance': 1.0, 'Retail Trade': -0.2,
    'Professional & Business Services': 0.0, 'Government': -0.7,
    'Leisure & Hospitality': -0.8, 'Manufacturing': -0.6,
    'Transportation & Warehousing': 0.8, 'Educational Services': 0.4,
    'Construction': 0.7, 'Information (Tech Sector)': -0.5,
    'Financial Activities': 0.5
}

df = pd.DataFrame({
    'Race_White': np.random.binomial(1, 0.85, size=n),
    'Age': np.random.normal(24, 3, size=n),
    'Gender_Male': np.random.binomial(1, 0.6, size=n),
    'Undergraduate': np.random.binomial(1, 0.75, size=n),
    'Full-Time': np.random.binomial(1, 0.75, size=n),
    'Program_Label': np.random.choice(list(program_effects.keys()), size=n),
    'GPA': np.random.normal(3.5, 0.3, size=n),
    'Engagements': np.random.uniform(0, 10, size=n),
    'Internships': np.random.uniform(0, 3, size=n),
    'Industry_Label': np.random.choice(list(industry_effects.keys()), size=n),
    'From_Utah': np.random.binomial(1, 0.6, size=n)
})

# Map program and industry scores
df['Program_Score'] = df['Program_Label'].map(program_effects)
df['Industry_Score'] = df['Industry_Label'].map(industry_effects)

# Simulate Job Placement as binary outcome
log_odds = (
    beta0
    + beta1 * df['Race_White']
    + beta2 * df['Age']
    + beta3 * df['Gender_Male']
    + beta4 * df['Undergraduate']
    + beta5 * df['Full-Time']
    + beta6 * df['Program_Score']
    + beta7 * df['GPA']
    + beta8 * df['Engagements']
    + beta9 * df['Internships']
    + beta10 * df['Industry_Score']
    + beta11 * df['From_Utah']
)
df['Job_Placement'] = np.random.binomial(1, expit(log_odds))

# Check class balance
print(df['Job_Placement'].value_counts())

# Fit logistic regression
X = df[['Race_White', 'Age', 'Gender_Male', 'Undergraduate', 'Full-Time',
        'Program_Score', 'GPA', 'Engagements', 'Internships',
        'Industry_Score', 'From_Utah']]
y = df['Job_Placement']

model = LogisticRegression()
model.fit(X, y)

# Compare true vs. estimated coefficients
true_betas = {
    'Race_White': beta1, 'Age': beta2, 'Gender_Male': beta3, 'Undergraduate': beta4,
    'Full-Time': beta5, 'Program_Score': beta6, 'GPA': beta7, 'Engagements': beta8,
    'Internships': beta9, 'Industry_Score': beta10, 'From_Utah': beta11
}

# Compare true vs. estimated coefficients (pretty print version)
print(f"{'Variable':<20} {'True β':>10} {'Estimated β':>15}")
print("-" * 45)
for name, coef in zip(X.columns, model.coef_[0]):
    print(f"{name:<20} {true_betas[name]:>10.2f} {coef:>15.2f}")
print(f"\n{'Intercept':<20} {beta0:>10.2f} {model.intercept_[0]:>15.2f}")

# Round selected columns to integers
df['Age'] = df['Age'].round(0).astype(int)
df['Engagements'] = df['Engagements'].round(0).astype(int)
df['Internships'] = df['Internships'].round(0).astype(int)

# Round all remaining numeric columns to 2 decimal places
df = df.round(2)

# Save to CSV
df.to_csv("simulated_job_placement.csv", index=False)