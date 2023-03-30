import escape_fractal_gen as efg
import numpy as np

def TEMP_EXAMPLE(x):
    return (x[0] + 1, x[1]) if x[0] < 5 else (x[0] - 10,x[1])

test = efg._get_escape_info(TEMP_EXAMPLE, (0.5, 0.5), 1000, 6)
print(test)




test_area = np.full((10, 10, 2), (0.5, 0.5))

output = np.zeros((10, 10))
for x, y in np.ndindex(*test_area.shape[:2]):
    results = efg._get_escape_info(TEMP_EXAMPLE, test_area[y, x], 1000, 6)
    output[y, x] = results[1]
    
print(output)