import pandas as pd
import scipy.stats as stats
import statsmodels.formula.api as smf
import plotly.express as px

df = pd.read_csv(f"./PAD_09_PD.csv", sep=";")

# 1)

female_income_df = df[df.Gender == 'Female']["Annual Income (k$)"]
male_income_df = df[df.Gender == 'Male']["Annual Income (k$)"]

statistic, pvalue = stats.ttest_ind(a=female_income_df, b=male_income_df)
alpha = 0.05
print(statistic, pvalue);

if pvalue < alpha:
  print("Reject H0 hypothesis")
  print("So there is significant difference)")
else:
  print("Don't reject H0 hypothesis")
  print("So there is no significant difference)")

print()


# 2)

df["Spending"] = df["Spending Score (1-100)"]
df["Income"] = df["Annual Income (k$)"]

model = smf.ols(formula="Spending ~ C(Gender) + Age + Income", data=df).fit()
print(model.summary())
print("P values:", model.pvalues.values)
print("Coef:", model.params.values)
print("Std err:", model.bse.values)
print()

print(df.corr())

px.imshow(df.corr(), color_continuous_scale="Agsunset", title="Correlation heatmap")

print()

model = smf.ols(formula="Spending ~ C(Gender) + Age", data=df).fit()
print(model.summary())