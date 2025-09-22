import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Generate Kangaroo Population
# -------------------------------
num_samples = 50000
kangaroo_population = np.random.normal(loc=12, scale=5, size=num_samples)  # mean=12 yrs, sd=5 yrs
kangaroo_population_df = pd.DataFrame(kangaroo_population, columns=["Population Values"])

# -------------------------------
# Sampling function
# -------------------------------
def sample_distr(n, num_iter, kangaroo_population_df):
    sample_stats = []
    for i in range(num_iter):
        sample_i = kangaroo_population_df["Population Values"].sample(n, replace=True)
        sample_i_stat = sample_i.mean()
        sample_stats.append(sample_i_stat)
    return sample_stats

# -------------------------------
# Streamlit App
# -------------------------------
def main():
    st.title("🦘 Law of Large Numbers: Kangaroo Age Simulation")

    st.write("This dashboard shows how the **Law of Large Numbers** works using a simulated kangaroo population.")

    # User inputs
    n = st.number_input("Enter Sample Size (n):", min_value=1, max_value=5000, value=50, step=1)
    num_iter = st.number_input("Enter Number of Iterations:", min_value=1, max_value=2000, value=200, step=10)

    # True population mean
    true_mean = kangaroo_population_df["Population Values"].mean()

    # Run sampling
    sample_means = sample_distr(n, num_iter, kangaroo_population_df)
    cum_avg = np.cumsum(sample_means) / np.arange(1, num_iter + 1)

    st.write(f"**True Population Mean Age:** {true_mean:.2f} years")

    # Plot: Sample Means over Iterations
    st.subheader("Convergence of Sample Means")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(range(1, num_iter + 1), sample_means, marker="o", linestyle="", alpha=0.6, label="Sample Mean per Iteration")
    ax.plot(range(1, num_iter + 1), cum_avg, color="red", label="Cumulative Average of Sample Means")
    ax.axhline(true_mean, color="black", linestyle="dashed", label="True Mean")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Sample Mean Age")
    ax.set_title(f"Sample Size = {n}, Iterations = {num_iter}")
    ax.legend()
    st.pyplot(fig)

    # Plot: Histogram of Sample Means
    st.subheader("Distribution of Sample Means")
    fig2, ax2 = plt.subplots(figsize=(7, 4))
    ax2.hist(sample_means, bins=20, color="skyblue", edgecolor="black", alpha=0.7)
    ax2.axvline(true_mean, color="red", linestyle="dashed", label="True Mean")
    ax2.set_xlabel("Sample Mean Age")
    ax2.set_ylabel("Frequency")
    ax2.set_title("Histogram of Sample Means")
    ax2.legend()
    st.pyplot(fig2)

if __name__ == "__main__":
    main()
