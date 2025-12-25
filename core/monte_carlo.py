import numpy as np

def monte_carlo_paths(S0, mu, sigma, T, N, steps):
    dt = T / steps
    paths = np.zeros((N, steps))
    paths[:, 0] = S0

    for t in range(1, steps):
        z = np.random.normal(size=N)
        paths[:, t] = paths[:, t-1] * np.exp(
            (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z
        )

    return paths
