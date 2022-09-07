'''
ResidencyMatch.py

This algorithm operates by reading an input file of the form

[residents | hospitals] preference 1, preference 2, preference 3, preference 4, ...

Any whitespace occurring in the input files is stripped off.

Usage:

    python ResidencyMatch.py [residents preference file] [hospitals preference file]

[Zachary Durham, Omar Al-Jafaari]

'''

import sys
import csv

class ResidencyMatch:

    # behaves like a constructor
    def __init__(self):
        '''
        Think of
        
            unmatchedHospitals
            residentsMappings
            hospitalsMappings
            matches
            
        as being instance data for your class.
        
        Whenever you want to refer to instance data, you must
        prepend it with 'self.<instance data>'
        '''
        
        # list of unmatched hospitals
        self.unmatchedHospitals = [ ]

        # list of unmatched residents
        self.unmatchedResidents = [ ]
        
        # dictionaries representing preferences mappings
        
        self.residentsMappings = { }
        self.hospitalsMappings = { }
        
        # dictionary of matches where mapping is resident:hospital
        self.matches = { }
        
        # read in the preference files
        
        '''
        This constructs a dictionary mapping a resident to a list of hospitals in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[1],'r'), delimiter = ',')
        for row in prefsReader:
            resident = row[0].strip()

             # all hospitals are initially unmatched
            self.unmatchedResidents.append(resident)

            # maps a resident to a list of preferences
            self.residentsMappings[resident] = [x.strip() for x in row[1:]]
            
            # initially have each resident as unmatched
            self.matches[resident] = None
        
        '''
        This constructs a dictionary mapping a hospital to a list of residents in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[2],'r'), delimiter = ',')
        for row in prefsReader:
            
            hospital = row[0].strip()
            
            # all hospitals are initially unmatched
            self.unmatchedHospitals.append(hospital)
            
            # maps a resident to a list of preferences
            self.hospitalsMappings[hospital] = [x.strip() for x in row[1:]] 
    
            
    def reportMatches(self):
        print(self.matches)
            
    def runMatch(self):
        while len(self.unmatchedHospitals) > 0:
            currentResident = self.unmatchedResidents[0]
            index = 0
            while index < len(self.residentsMappings[currentResident]) and self.matches[currentResident] is None:
                bestHospital = (self.residentsMappings[currentResident])[index]
                if bestHospital in self.unmatchedHospitals:
                    if self.matches[currentResident] is None:
                        (self.matches[currentResident]) = bestHospital
                        self.unmatchedHospitals.remove(bestHospital)
                        self.unmatchedResidents.pop(0)
                    else:
                        for i in range(len(self.residentsMappings[currentResident])):
                            hospital = self.residentsMappings[currentResident][i]
                            if self.hospitalsMappings[hospital].index(currentResident) > self.residentsMappings[currentResident].index((self.matches[currentResident])):
                                self.unmatchedHospitals.append((self.matches[currentResident])[0:1])
                                (self.matches[currentResident]) = bestHospital
                index += 1


if __name__ == "__main__":
   
    # some error checking
    if len(sys.argv) != 3:
        print('ERROR: Usage\n python ResidencyMatch.py [residents preferences] [hospitals preferences]')
        quit()

    # create an instance of ResidencyMatch 
    match = ResidencyMatch()

    # now call the runMatch() function
    match.runMatch()
    
    # report the matches
    match.reportMatches()



