import pandas as pd
df = pd.read_csv("simulated_job_placement.csv")

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors
import pandas as pd

# Define high engagement as 7+ for illustration
df['High_Engaged'] = (df['Engagements'] >= 7).astype(int)

# Predictors (excluding Engagement itself)
covariates = ['Race_White', 'Age', 'Gender_Male', 'Undergraduate', 'Full-Time',
              'Program_Score', 'GPA', 'Internships', 'Industry_Score', 'From_Utah']

# Fit logistic model for propensity scores
ps_model = LogisticRegression()
ps_model.fit(df[covariates], df['High_Engaged'])

# Add predicted propensity scores
df['propensity'] = ps_model.predict_proba(df[covariates])[:, 1]

# Split treated/control
treated = df[df['High_Engaged'] == 1]
control = df[df['High_Engaged'] == 0]

# Fit nearest neighbor on propensity scores
nn = NearestNeighbors(n_neighbors=1)
nn.fit(control[['propensity']])

# Find nearest neighbors
distances, indices = nn.kneighbors(treated[['propensity']])
matched_control = control.iloc[indices.flatten()].copy()
matched_control['matched_pair_id'] = treated.index

# Combine matched pairs
matched_df = pd.concat([treated, matched_control])

effect = matched_df.groupby('High_Engaged')['Job_Placement'].mean()
print(f"\nEstimated Causal Effect:\n{effect[1] - effect[0]:.3f} (High - Low Engagement)")