import numpy as np
import pandas as pd
import pymc as pm
import arviz as az
from sklearn.preprocessing import StandardScaler

# Set seed and sample size
np.random.seed(42)
n = 2000

# True parameter values
beta0 = -12.5
beta1 = 0.3    # Race_White
beta2 = 0.3    # Age
beta3 = 0.3    # Gender_Male
beta4 = 0.1    # Undergraduate
beta5 = 0.5    # Full-Time
beta6 = 0.3    # Program Score
beta7 = 0.5    # GPA
beta8 = 0.7    # Engagements (target causal effect)
beta9 = 0.9    # Internships
beta10 = 0.3   # Industry Score
beta11 = -0.3  # From Utah

# Program and industry mappings
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

# Simulate the dataset
df = pd.DataFrame({
    'Race_White': np.random.binomial(1, 0.85, size=n),
    'Age': np.random.normal(24, 3, size=n),
    'Gender_Male': np.random.binomial(1, 0.6, size=n),
    'Undergraduate': np.random.binomial(1, 0.75, size=n),
    'Full-Time': np.random.binomial(1, 0.75, size=n),
    'Program_Label': np.random.choice(list(program_effects.keys()), size=n),
    'GPA': np.random.normal(3.5, 0.3, size=n),
    'Engagements': np.random.randint(0, 11, size=n),
    'Internships': np.random.randint(0, 4, size=n),
    'Industry_Label': np.random.choice(list(industry_effects.keys()), size=n),
    'From_Utah': np.random.binomial(1, 0.6, size=n)
})

df['Program_Score'] = df['Program_Label'].map(program_effects)
df['Industry_Score'] = df['Industry_Label'].map(industry_effects)

# Linear combination for log-odds
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

df['Job_Placement'] = np.random.binomial(1, 1 / (1 + np.exp(-log_odds)))

# Scale features for PyMC
features = ['Race_White', 'Age', 'Gender_Male', 'Undergraduate', 'Full-Time',
            'Program_Score', 'GPA', 'Engagements', 'Internships',
            'Industry_Score', 'From_Utah']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])
y = df['Job_Placement'].values

# Bayesian logistic regression using PyMC
with pm.Model() as model:
    alpha = pm.Normal('alpha', mu=0, sigma=1)
    betas = pm.Normal('betas', mu=0, sigma=1, shape=X_scaled.shape[1])
    logits = alpha + pm.math.dot(X_scaled, betas)
    theta = pm.Deterministic('theta', pm.math.sigmoid(logits))
    y_obs = pm.Bernoulli('y_obs', p=theta, observed=y)

    # Sample from the posterior
    trace = pm.sample(1000, tune=1000, chains=2, target_accept=0.9, return_inferencedata=True)

# Summarize posterior
az.summary(trace, var_names=["alpha", "betas"], round_to=2)

import arviz as az
import matplotlib.pyplot as plt

# Trace plot (includes density + samples for each parameter)
az.plot_trace(trace, combined=True)
plt.suptitle("Posterior Traces of Coefficients", fontsize=16)
plt.tight_layout()
plt.show()