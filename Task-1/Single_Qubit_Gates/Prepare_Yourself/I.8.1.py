dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def prepare_state():
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY OPERATIONS TO PREPARE THE TARGET STATE:

    #Deal with amplitudes:
    qml.Hadamard(wires=0)

    #Deal with phase:
    qml.RZ(5 * np.pi/4.0, wires=0)

    return qml.state()
