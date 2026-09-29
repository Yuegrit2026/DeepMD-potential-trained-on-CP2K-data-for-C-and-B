The 00.data folder contains the data produced by CP2K using molecular dynamics simulation, as well as the data converted for train using trans.py; 
the 01.train folder contains the various files generated when using DeepMD-kit to train the data, including the deepmd potential; 
the 03.train folder contains the relevant files for the deposition simulation using LAMMPS.

Since this is preliminary research, the variable-temperature molecular dynamics simulations with CP2K were not fully completed, 
and the structures of the crystal and defect states were not considered. In addition, the classical molecular dynamics simulations 
using LAMMPS were only run for a very short time.
