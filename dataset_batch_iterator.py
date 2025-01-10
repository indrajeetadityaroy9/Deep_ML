"""
a batch iterable function that samples in a numpy array X and an optional numpy array y. 
The function should yield batches of a specified size. If y is provided, the function should yield batches of (X, y) pairs; otherwise, it should yield batches of X only.
"""

import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	n_samples = len(X)
	indices = np.arange(n_samples)
	batches = []

	for start_idx in range(0, n_samples, batch_size):
		end_idx = start_idx + batch_size
		batch_indices = indices[start_idx:end_idx]

		X_batch = X[batch_indices].tolist()

		if y is not None:
			y_batch = y[batch_indices].tolist()
			batches.append((X_batch, y_batch))
		else:
			batches.append(X_batch)
	
	return batches