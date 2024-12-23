# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from iminuit import Minuit, cost
from scipy.stats import truncnorm, uniform

# Seed for reproducibility
np.random.seed(42)

# Define global parameters for distributions
x_lim = [0.0, 5.0]
y_lim = [0.0, 10.0]
mu = 3.0
sig = 0.3
beta = 1.0
m = 1.4
f = 0.6
lam = 0.3
mub = 0.0
sigb = 2.5

params = {
    "f": f,
    "beta": beta,
    "m": m,
    "mu": mu,
    "sig": sig,
    "lam": lam,
    "mub": mub,
    "sigb": sigb
}

# Signal and background probability density functions

def signal_density_x(x, beta, m, mu, sig):
    """Signal PDF for X dimension"""
    pdf = truncnorm.pdf(x, (x_lim[0] - mu) / sig, (x_lim[1] - mu) / sig, loc=mu, scale=sig)
    return np.where((x >= x_lim[0]) & (x <= x_lim[1]), pdf, 0.0)

def background_density_x(x):
    """Background PDF for X dimension"""
    return uniform.pdf(x, loc=x_lim[0], scale=x_lim[1] - x_lim[0])

def signal_density_y(y, lam):
    """Signal PDF for Y dimension"""
    scale = 1 / lam
    pdf = truncnorm.pdf(y, (y_lim[0] - scale) / scale, (y_lim[1] - scale) / scale, loc=scale, scale=scale)
    return np.where((y >= y_lim[0]) & (y <= y_lim[1]), pdf, 0.0)

def background_density_y(y, mub, sigb):
    """Background PDF for Y dimension"""
    pdf = truncnorm.pdf(y, (y_lim[0] - mub) / sigb, (y_lim[1] - mub) / sigb, loc=mub, scale=sigb)
    return np.where((y >= y_lim[0]) & (y <= y_lim[1]), pdf, 0.0)

# Combined density functions

def total_density_x(x, f, beta, m, mu, sig):
    return f * signal_density_x(x, beta, m, mu, sig) + (1 - f) * background_density_x(x)

def total_density_y(y, f, lam, mub, sigb):
    return f * signal_density_y(y, lam) + (1 - f) * background_density_y(y, mub, sigb)

# Sampling functions

def generate_samples(n_samples, params):
    """Generate signal and background samples"""
    n_signal = int(params["f"] * n_samples)
    n_background = n_samples - n_signal

    x_signal = np.random.normal(params["mu"], params["sig"], n_signal)
    y_signal = np.random.exponential(1 / params["lam"], n_signal)

    x_background = np.random.uniform(x_lim[0], x_lim[1], n_background)
    y_background = np.random.normal(params["mub"], params["sigb"], n_background)

    x_samples = np.concatenate([x_signal, x_background])
    y_samples = np.concatenate([y_signal, y_background])

    return x_samples, y_samples

# Negative log-likelihood function

def negative_log_likelihood(params, x_samples, y_samples):
    """Calculate the negative log-likelihood for combined density"""
    f, beta, m, mu, sig, lam, mub, sigb = params
    density_x = total_density_x(x_samples, f, beta, m, mu, sig)
    density_y = total_density_y(y_samples, f, lam, mub, sigb)

    likelihood = density_x * density_y
    return -np.sum(np.log(np.maximum(likelihood, 1e-10)))  # Avoid log(0)

# Fit function

def fit_mle(x_samples, y_samples, initial_params):
    """Perform maximum likelihood estimation using Minuit"""
    def cost_function(f, beta, m, mu, sig, lam, mub, sigb):
        return negative_log_likelihood([f, beta, m, mu, sig, lam, mub, sigb], x_samples, y_samples)

    mi = Minuit(
        cost_function,
        f=initial_params["f"],
        beta=initial_params["beta"],
        m=initial_params["m"],
        mu=initial_params["mu"],
        sig=initial_params["sig"],
        lam=initial_params["lam"],
        mub=initial_params["mub"],
        sigb=initial_params["sigb"]
    )

    mi.limits = {
        "f": (0, 1),
        "beta": (0, None),
        "m": (0, None),
        "mu": (None, None),
        "sig": (1e-3, None),
        "lam": (1e-3, None),
        "mub": (None, None),
        "sigb": (1e-3, None)
    }

    mi.migrad()
    mi.hesse()

    if not mi.valid or mi.fmin.has_parameters_at_limit or mi.fmin.hesse_failed:
        print("Fit failed.")
        return None, None

    return mi.values, mi.errors

# Bootstrap study

def bootstrap_analysis(n_trials, n_samples, params):
    """Perform bootstrap analysis"""
    bootstrap_results = []
    bootstrap_errors = []

    for _ in tqdm(range(n_trials)):
        x_samples, y_samples = generate_samples(n_samples, params)
        vals, errs = fit_mle(x_samples, y_samples, params)

        if vals is not None:
            bootstrap_results.append(vals)
            bootstrap_errors.append(errs)

    return np.array(bootstrap_results), np.array(bootstrap_errors)

# Visualization

def plot_results(bootstrap_results):
    """Plot bootstrap results"""
    labels = ["f", "beta", "m", "mu", "sig", "lam", "mub", "sigb"]
    for i, label in enumerate(labels):
        plt.hist(bootstrap_results[:, i], bins=50, alpha=0.7, label=label)
        plt.title(f"Bootstrap Distribution of {label}")
        plt.xlabel(label)
        plt.ylabel("Frequency")
        plt.legend()
        plt.savefig("boot_test.pdf")

        plt.show()


n_samples = 1000
n_trials = 100

    # Generate bootstrap results
bootstrap_results, bootstrap_errors = bootstrap_analysis(n_trials, n_samples, params)

    # Plot results
plot_results(bootstrap_results)