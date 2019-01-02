"""Main server file.  Calculates SPRs every 15 seconds."""
# External imports
import time
# Internal imports
import SPR

while True:
    SPR.SPRCalculator()
    time.sleep(5)
