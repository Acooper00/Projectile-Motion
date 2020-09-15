# Projectile-Motion
Simulates the motion of a projectile with some account for air resistance

Priciples Used:
- The object is moved forward the appropriate distance due to its velocity and angle.
- The vertical and horizontal components of the object's velocity are calculated from its velocity and angle
- The force of air resistace is calculated using the equation F = -(k/2)(v^2), where k is a predetermined constant calculated from the parameters of the object, and v is the velocity of the object
- The vertical and horizontal components of the force of air resistace is calculated
- The vertical and horizontal components of the force on the object is calculated using the resolved forces of air resistance and the force of gravity, divided by the mass of the object
- The vertical and horizontal components of the object's velocity are updated by adding the resolved accelerations.
- The new velocity and angle then calculated
- The value of time is then incremented

The simulation assumes no wind or turbulence. It does also not account for any spin of the object, or any changes to the objects parameters while in the air.


The format of the ".dat" files:

- A .dat file is created automatically in the "Data" directory when the program is run. It's name is the time that the simulation was run in the format "YYYY_mm_dd_HH:MM:SS.dat"

- The file begins with all variables in the "simulationvars" array being written in the format of: NAME (padded to 40 characters with spaces), "- ", VALUE. Each variable is on a seperate line.
- There is then an empty line.
- Each variable from the "settingvars" is then written in the same format as above.
- There is an empty line.
- The value of each variable listed in the "datavars" array at each time increment of the simulation is then displayed as tab seperated text with headers.
