nodeview
========

This is a new version of my nodeview tool that will aim to provide a unified
view of clusters running Torque, Slurm, SGE, or whatever other resource manager
is available.

The first incarnation was written in Perl and was locked to Torque as provided
by Rocks.  The second incarnation had very limited functionality and was
implemented in Python.  This version aims to work with Torque/Moab, Cray XT,
Slurm, and everything else via a more modular and extensible design.
