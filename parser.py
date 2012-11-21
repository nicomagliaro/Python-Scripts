import ConfigParser
import os.path

class ParserINI(object):
    """attributes may need additional manipulation"""
    def __init__(self, conffile='config.ini'):
        """section to retun all options on, formatted as an object
        transforms all comma-delimited options to lists
        comma-delimited lists with colons are transformed to dicts
        dicts will have values expressed as lists, no matter the length
        """
        try:    
            self.parser = ConfigParser.RawConfigParser()
            self.conffile = conffile
            #self.parser.readfp(self.conffile, 'r')
            self.parser.read(self.conffile)
        except ConfigParser.ParsingError, err:
            print 'Could not parse:', err

    def get ( self, SECTION, OPTION ):
        try:
            return self.parser.get(SECTION, OPTION)
        except ConfigParser.NoSectionError: 
            return None
        except ConfigParser.NoOptionError: 
            return None    

    def getInifile ( self, SECTION, OPTION, DEFAULT ):          
        if self.parser.has_section ( SECTION ):
            #print 'Has Section'
            if self.parser.has_option ( SECTION, OPTION ):
                #print 'Has Option'
                Value = self.parser.get ( SECTION, OPTION ).strip()
            else:
                Value = DEFAULT
        else:
            Value = DEFAULT
        return Value

    def writeInifile ( self, SECTION='Testsection', OPTION='Item', VALUE='wheeee' ):
        if not self.conffile:
            return
        if not self.parser.has_section ( SECTION ):
            self.parser.add_section(SECTION)
        self.parser.set(SECTION, OPTION, VALUE)
        self.save()

    def getSection ( self, SECTION ):       
        try: 
            for item in self.parser.items(SECTION):
                print item
        except ConfigParser.NoSectionError: 
            return None    
        
    def remove ( self, SECTION, OPTION ):
        self.parser.remove_option(SECTION, OPTION)
        self.save() 

    def removeSection ( self, SECTION ):    
        self.parser.remove_section(SECTION)
        self.save()             

    def save ( self ):
        try:
            with open(self.conffile, 'w') as f:
                self.parser.write(f)    
        finally:
            f.close()

if __name__ == "__main__":

    Data = ParserINI('config.ini')
    #Data.writeInifile('database','dhuser','root')
    #Data.getSection('database')
    #print Data.getInifile('database','dbuser')
    #print Data.get('database','dbuser')
    #Data.remove('database','dbuser')
    Data.removeSection('database')