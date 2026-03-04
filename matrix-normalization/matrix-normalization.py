import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    m = np.asarray(matrix)
    m = m.astype(np.float64)
    if m.ndim != 2:
        return None
    height = m.shape[0]
    width = m.shape[1]
    if norm_type == 'l2':
        if axis == 0:
            temp = np.pow(m.T, 2)
            m = m.T
            for i in range(0, width):
                norm = np.sqrt(np.sum(temp[i]))
                if norm != 0:
                    m[i] /= norm
            m = m.T
            return m
        if axis == 1:
            temp = np.pow(m, 2)
            for i in range(0, height):
                norm = np.sqrt(np.sum(temp[i]))
                if norm != 0:
                    m[i] /= norm
            return m
        if axis == None:
            m /= np.sqrt(np.sum(np.pow(m, 2)))
            return m
    if norm_type == 'l1':
        if axis == 0:
            temp = np.abs(m.T)
            m = m.T
            for i in range(0, width):
                norm = np.sum(temp[i])
                if norm != 0:
                    m[i] /= norm 
            m = m.T
            return m
        if axis == 1:
            temp = np.abs(m)
            for i in range(0, height):
                norm = np.sum(temp[i])
                if norm != 0:
                    m[i] /= norm 
            return m
        if axis == None:
            m /= np.sqrt(np.sum(np.abs(m)))
            return m
    if norm_type == 'max':
        if axis == 0:
            temp = np.abs(m.T)
            m = m.T
            for i in range(0, width):
                norm = np.max(temp[i])
                if norm != 0:
                    m[i] /= norm 
            m = m.T
            return m
        if axis == 1:
            temp = np.abs(m)
            for i in range(0, height):
                norm = np.max(temp[i])
                if norm != 0:
                    m[i] /= norm 
            return m
        if axis == None:
            m /= np.sqrt(np.max(np.abs(m)))
            return m
    return None
    pass