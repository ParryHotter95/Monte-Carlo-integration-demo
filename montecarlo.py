import matplotlib.pyplot as plt
import random

# Let's define some mathematical function
def function(x):
    return 5 * x**3 + 0.5


def mc(ax, function, limits, samples=5000):
    """
    This function performs Monte Carlo integration on provided function, within specified limits,
    using defined number of random sample points, and plotting it's results on passed Matplotlib's
    Axes object (ax)
    """
    ax.set_title(f"{samples} samples")
    # Prepare two lists for function's plot points, x and y
    function_x, function_y = [], []
    x_limits = limits

    # Generate function's points for visualization
    for sample in range(samples):
        x = x_limits[0] + sample * (x_limits[1] - x_limits[0]) / samples
        function_x.append(x)
        function_y.append(function(x))

    # Plot the function's visualization
    ax.plot(function_x, function_y)
    # Find function's minimum and maximum values within integration limits
    y_limits = (min(function_y), max(function_y))
    counter = 0
    random.seed(69456431344)  # constant seed for reproducible results

    for i in range(samples):
        # generate random points in rectangle enclosed by integration limits
        # in x axis, and function's extrema in y axis
        x = random.uniform(x_limits[0], x_limits[1])
        y = random.uniform(y_limits[0], y_limits[1])
        if y <= function(x) and y > 0:
            # if generates point is under function's curve, and positive
            # draw it as a green cross
            ax.plot(x, y, "gx")
            # and increase the counter by one
            counter += 1
        elif y >= function(x) and y < 0:
            # if generates point is under function's curve, and negative
            # draw it as a red cross
            ax.plot(x, y, "rx")
            # and decrease the counter by one
            counter -= 1
        else:
            ax.plot(x, y, "kx")
            # in any other circumstance the point is either positive
            # and above function's plot, or negative and beneath
            # function's plot, we don't count these points and mark
            # them with black crosses

    # calculate total area of rectangle we were shooting at with random points
    total_plot_area = (x_limits[1] - x_limits[0]) * (y_limits[1] - y_limits[0])
    # multiply it by a ratio of counter value and total samples number
    # to receive integration result
    result = total_plot_area * counter / samples
    text_location = (
        x_limits[0] + 3 * (x_limits[1] - x_limits[0]) / 4,
        y_limits[0] + (y_limits[1] - y_limits[0]) / 4,
    )
    text = f"A = {result:5.4}"
    ax.text(
        text_location[0],
        text_location[1],
        text,
        bbox={"facecolor": "white", "alpha": 0.9, "pad": 5},
    )
    print(result)


# Let's use polynominal we defined before and integrate it between x= -1 and 1
limits = (-1, 1)
# We will compare results obtained with 100, 500 and 2000 samples
samples = (100, 500, 2000)
# Generate a figure and three axes
fig, axs = plt.subplots(len(samples))
# For each axes and number of samples
for ax, samples_number in zip(axs, samples):
    # Run Monte Carlo function with parameters we defined before
    mc(ax, function, limits, samples=samples_number)
# Make some visual improvements for readibility
plt.subplots_adjust(hspace=0.5)
fig.set_size_inches(8, 8)
# And show the results
fig.show()
# As we can see, the calculated area converges to the exact result (1.000)
# with increasing number of samples
