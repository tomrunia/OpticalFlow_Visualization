# Optical Flow Visualization

Python port of the optical flow visualization: [people.csail.mit.edu/celiu/OpticalFlow/](https://people.csail.mit.edu/celiu/OpticalFlow/).
This implementation is based on the color wheel presented in: 

```
S. Baker, D. Scharstein, J. Lewis, S. Roth, M. J. Black, and R. Szeliski. 
A database and evaluation methodology for optical flow. 
In Proc. IEEE International Conference on Computer Vision (ICCV), 2007.
```

## Usage

One-liner: `flow_color = flow_vis.flow_to_color(flow_uv, convert_to_bgr=False)`

## Examples visualizations 

Example visualization from the MPI Sintel Dataset:

![MPI Sintel 01](./data/mpi-sintel-01.png)

![MPI Sintel 02](./data/mpi-sintel-03.png)

![MPI Sintel 03](./data/mpi-sintel-02.png)




