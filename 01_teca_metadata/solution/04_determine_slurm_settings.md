In this manual step, examine the output from the "test teca_cf_restripe" step to (1) make sure it worked as expected, (2) check the size of the files, and (3) check the run time.

You can use information from (2) to determine whether you have adequate scratch space for a run on the full dataset.  You can use information from (3) to set the SLURM settings as appropriate.  Since `teca_cf_restripe` tends to scale quite well, I use the following formula to figure out how many cores and nodes to request:

$$ N = \frac{\hat{t}}{\hat{s}/\hat{N}} \frac{s}{t}$$
$$ n = N \cdot p$$

| Variable | Description |
| -------- | ----------- |
| n        | Approx. number of cores to request | 
| $\hat{t}$| Runtime of test run |
| $\hat{s}$| Number of steps in test run |
| $\hat{N}$| Number of nodes in test run |
| p        | Cores-per-node (in test and production) |
| s        | Number of steps in full run (see output from `teca_metadata_probe`)|
| t        | Desired runtime of production run |
| n        | Number of cores to use in production (the number for `srun -n`)
| N        | Number of nodes in production run |


In my test, I had $p=32$, $\hat{N}=4$, $\hat{s}=1536$, and $\hat{t} = 280 \text{s}$.  Examination of the output of `teca_metadata_probe` gives me $s=385704$. And I want $t \approx 60 \text{min.} = 3600 \text{s}$.  Plugging in to that formula gives $N \approx 78$ and $n = 2496$.  I would increase $t$ by about 25% to give some buffer room.  Note though, that when I did a similar test on a weekend day, $\hat{t}$ was about half this time, so I/O costs can vary dramatically depending on who is doing what at NERSC; I ended up running on $N = 40$ nodes (and processing several additional 3D variables) and the run completed in less than 60 minutes.

It can be worth running the restripe test a few times and for a few different values of $\hat{s}$ to get a better handle on the estimate and the amount by which I/O variability might be a factor.

