def measure_state(state, num_meas):
    """Simulate a quantum measurement process.

    Args:
        state (np.array[complex]): A normalized qubit state vector.
        num_meas (int): The number of measurements to take

    Returns:
        np.array[int]: A set of num_meas samples, 0 or 1, chosen according to the probability
        distribution defined by the input state.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # COMPUTE THE MEASUREMENT OUTCOME PROBABILITIES
    probabilities = np.abs(state)**2

    # RETURN A LIST OF SAMPLE MEASUREMENT OUTCOMES
    measurements = np.array([0, 1])
    outcomes = np.random.choice(measurements, size=num_meas, p=probabilities)
    
    return outcomes