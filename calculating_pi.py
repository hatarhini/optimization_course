# import libraries
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--sample_size", type=int, required=True)
parser.add_argument("--step_size", type=int, required=True)
parser.add_argument("--window_size_ma", type=int, required=True)

args = parser.parse_args()

sample_size = args.sample_size
step_size = args.step_size
window_size = args.window_size_ma


def estimate_pi(sample_size: int) -> float:
    print("sample_size=", sample_size)
    # generate random samples
    random_samples = np.random.random_sample((sample_size, 2))
    # count number of points inside the circle

    points_inside_circle = np.where(np.linalg.norm(random_samples, axis=1) <= 1, 1, 0)

    pi_hat = 4 * np.sum(points_inside_circle) / sample_size
    return pi_hat


def moving_average(data, window_size):
    cumsum = np.cumsum(data)
    cumsum[window_size:] = cumsum[window_size:] - cumsum[:-window_size]
    return cumsum[window_size - 1 :] / window_size


pi_hat_sample = list(
    map(
        estimate_pi,
        range(100, sample_size, step_size),
    )
)
pi_hat_ma = moving_average(pi_hat_sample, window_size)
# %%
plt.scatter(range(100, sample_size, step_size), pi_hat_sample)
plt.plot(
    list(range(100, sample_size, step_size))[window_size - 1 :],
    pi_hat_ma,
    color="red",
    label=f"Moving Average (Window Size={window_size})",
)
plt.ylim(3.141, 3.142)
plt.show()
