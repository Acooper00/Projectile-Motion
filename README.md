# Projectile-Motion
Simulates the motion of a projectile with some account for air resistance

The format of the ".dat" files:

A .dat file is created automatically in the "Data" directory when the program is run. It's name is the time that the simulation was run in the format "YYYY_mm_dd_HH:MM:SS.dat"

The file begins with all variables in the "simulationvars" array being written in the format of: NAME (padded to 40 characters with spaces), "- ", VALUE. Each variable is on a seperate line.
There is then an empty line.
Each variable from the "settingvars" is then written in the same format as above.
There is an empty line.
The value of each variable listed in the "datavars" array at each time increment of the simulation is then displayed as tab seperated text with headers.
