class ConfigurationParameters:

    def __init__(self):
        pass
 
    def recreateConfigurationFile(self):
        out = open('config.data','w')
        try:
            out.write("CommunicationRadius 10")
            out.close()
        except:
            print("Error recreating configuration file!")
