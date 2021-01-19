# not necessary, can be avoided with loops and if-statement but are more concise

# The classes a student is registered for
classes_registered = ['IEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']

# Make a list of only the ITEC classes
only_itec = [c for c in classes_registered if c.startswith('ITEC')]
print(only_itec)


# Record temperatures ever day. Record -1 if not possible to take measurement.
high_temps = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]