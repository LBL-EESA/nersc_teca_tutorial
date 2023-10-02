# Toolkit for Extreme Climate Analysis (TECA) Tutorial

## What will I learn?
The primary goal is that you come away from this tutorial inspired and enabled to use the [Toolkit for Extreme Climate Analysis (TECA)](https://teca.readthedocs.io/en/latest/?badge=latest#) in your own research.  Specifically, by the end of this tutorial, you will be able to:

* apply existing TECA extremes detection tools to a climate dataset
* write a custom TECA application using Python
* create a new TECA algorithm in Python

## How will I learn?

This tutorial will use a combination of short lectures interspersed with lengthy practical exercises on a real supercomputing system.

## What do I need to know in advance?

This tutorial assumes that participants

* are proficient in the use of Unix-type command line systems
* have some familiarity with programming (Python experience isn’t strictly necessary; if you know R, for example, the skills should be transferable for this tutorial)
* have some experience with netCDF-based climate data
* have accounts on NERSC
* have access to data in the m3522 CFS directory at NERSC

## Who is leading the tutorial?
I’m Travis A. O’Brien, an Assistant Professor at Indiana University Bloomington and Visiting Faculty at Lawrence Berkeley National Lab.  My research focuses on understanding the factors that control variability and trends in extreme weather. Along with Dr. Mark Risser, I co-lead the Computational and Statistical Infrastructure team within the Calibrated and Systematic Characterization, Attribution, and Detection of Extreme ([CASCADE](https://cascade.lbl.gov/)) project, which is the main project that sponsors the development of TECA.  I am also one of the developers of TECA (Dr. Burlen Loring is the primary developer).

## What will we do in the tutorial?

This three-hour tutorial will roughly follow this outline:

| Lecture | Duration | Mode of Instruction | Activity |
| ------- | -------- | ------------------- | -------- |
| 1       | 15 min | Lecture | Overview of TECA and its three main ways of being used |
| 1       | 20 min | Lab | Use `teca_metadata_probe` to get the properties of a large netCDF dataset |
| 1       | 15 min | Lab | Use `teca_cf_restripe` to subselect & rewrite a dataset |
| 2       | 10 min | Lecture | Custom TECA Python applications |
| 2       | 50 min | Lab | Write and test `teca_heatwave_detect.py` |
| 3       | 30 min | Lab | Continue work on `teca_heatwave_detect.py` |
| 3       | 20 min | Lab | Use `teca_temporal_reduce` to generate composites of heatwave conditions |
| 3       | 10 min | Discussion | Other options TECA applications |

