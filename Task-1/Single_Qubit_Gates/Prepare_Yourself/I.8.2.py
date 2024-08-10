dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def prepare_state():
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY OPERATIONS TO PREPARE THE TARGET STATE:

    #Dealing with amplitudes:
    qml.RX(np.pi/3, wires=0) #also deals with the phase

    return qml.state()
