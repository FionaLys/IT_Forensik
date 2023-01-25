# E(w) = 6w^2 + 3w - 5
# E'(w) = 12w + 3
# eta = 0,1

def loss(w1):
    # w^(t+1) = w(t) - eta * E(w(t))
    eta = 0.1
    E = 6*w1**2+3*w1-5
    return (w1 - eta * E)