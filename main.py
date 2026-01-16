## create window to select type of server and region
## close that window and create new window to show list of servers based on previous selection
## close that window and create a new window to show details of selected server
##   if that server is down, show option to check server

## server checker will use the blizzard API to check server status, and create a notification when server comes up

import sys

def main() -> int:
    # select region
    regionList = getRegionList()
    

    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)



def getRegionList() -> list:
    regionList = []


    return regionList