from dotenv import load_dotenv
from os import getenv
import requests
import getopt
import enum
import sys


"""Print colours to terminal
https://www.geeksforgeeks.org/print-colors-python-terminal/"""
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


# Can't exit program here, as this would screw up cmd line key option
if load_dotenv('.env'):
    if getenv('NHSKEY'):
        prGreen("""Loaded NHS API Key""")
    else:
        prRed("""Couldn't load key - use: make setup""")
else:
    prRed("""Couldn't load .env file""")


# move to wrapper
class organisID(enum.Enum):
    AreaTeam = 'LAT'
    CareHome = 'SCL'
    Clinic = 'CLI'
    ClinCommisGrp = 'CCG'
    Dentist = 'DEN'
    GP = 'GPB'
    GPPractice = 'GPP'
    GenDirOfServ = 'GDOS'
    GenServDir = 'GSD'
    HealthAuth = 'HA'
    HealthWell = 'HWB'
    Hospital = 'HOS'
    LocalAuth = 'LA'
    MinorInj = 'MIU'
    Opticians = 'OPT'
    Pharmacy = 'PHA'
    RegionalArea = 'RAT'
    SocialProv = 'SCP'
    StratHealth = 'SHA'
    Sustain = 'STP'
    Trust = 'TRU'
    UrgentCare = 'UC'


# move to wrapper
class selections(enum.Enum):
    Name = "OrganisationName"
    Address = "Address1,Address2,Address3,City,County,Postcode"
    OpenTimes = "OpeningTimes"
    Contact = "Contacts"
    Alias = "OrganisationAliases"
    Type = "OrganisationTypeID"


# move to handler
def dispatchRequest(reqBody: str,
                    url="https://api.nhs.uk/service-search/search/?api-version=1",
                    reqHeaders={"subscription-key": getenv("NHSKEY"), "Content-Type": "application/json"}) -> requests.Response:
    """Dispatch a post request to the NHS search"""

    # Should I strip REST request queries?
    prGreen("Using URL:")
    print(url)
    prGreen("Dispatching with headers of:")
    print(reqHeaders)
    prGreen("Dispatching with body of:")
    print(reqBody)

    return requests.post(url, headers=reqHeaders, data=reqBody)


# move to handler
def constructFilterStr(orgIDs: list(organisID)) -> str:
    return f"OrganisationTypeID eq '{orgIDs[0].value}'" if len(orgIDs) == 1 else " or ".join(
        f"(OrganisationTypeID eq '{orgID.value}')" for orgID in orgIDs)


# move to handler
def constructSelectStr(selections: list(selections)) -> str:
    return ",".join([f"{selection.value}" for selection in selections])


# move to wrapper
def searchByPostcode(postCode: str, orgTypes: list(organisID), select: list(selections) = [selections.Name]) -> requests.Response:
    url = "https://api.nhs.uk/service-search/search-postcode-or-place?api-version=1&search=" + \
        postCode.replace(" ", "")

    return dispatchRequest(f'''{{"filter": "{constructFilterStr(orgTypes)}",
                       "select": "{constructSelectStr(select)}",
                       "top": 2}}'''.strip(), url)


# move to wrapper
def searchByName(name: str, orgTypes: list(organisID), select: list(selections) = [selections.Name]) -> requests.Response:
    return dispatchRequest(f'''{{"filter": "{constructFilterStr(orgTypes)}",
    "searchFields": "OrganisationName,OrganisationAliases",
    "search": "{name}",
    "select": "{constructSelectStr(select)}",
    "top": 2,
    "skip": 0,
    "count": true}}'''.strip())


if __name__ == "__main__":

    organisation: list(organisID) = []
    select: list(selections) = []
    by = ""
    query = ""

    try:
        opts, remainder = getopt.gnu_getopt(
            sys.argv[1:], 'o:s:b:query', ['organisation=', 'select=', 'by=', 'query='])
    except getopt.GetoptError as err:
        print('Argument Error:', err)
        sys.exit(1)

    print(f"args: {opts}")

    for opt, arg in opts:
        if opt in ('-o', '--organisation'):
            try:
                for org in arg.split(","):
                    organisation.append(organisID[org])

            except KeyError as err:
                print(
                    """\033[91mIncorrect args.\033[00m They must be comma seperated with no spaces.""")
                if input(" Do you want to see all available organisation arguments?\n (y/n) : ") == "y":
                    for i, org in enumerate(organisID):
                        print(org.name, end=',' if i < (
                            len(organisID)-1) else '\n')

                sys.exit(1)

        elif opt in ('-s', '--select'):
            try:
                for sel in arg.split(","):
                    select.append(selections[sel])

            except KeyError as err:
                print(
                    """\033[91mIncorrect args.\033[00m They must be comma seperated with no spaces.""")
                if input(" Do you want to see all available select arguments?\n (y/n) : ") == "y":
                    for i, sel in enumerate(selections):
                        print(sel.name, end=',' if i < (
                            len(selections)-1) else '\n')

                sys.exit(1)

        elif opt in ('-b', '--by'):
            acceptable = ["coord", "postplace", "name", "ods"]
            if arg in acceptable:
                by = arg
            else:
                print(
                    f"""\033[91mIncorrect args: {opts}\033[00m They must be comma seperated with no spaces.""")
                if input(" Do you want to see all available arguments to search by?\n (y/n) : ") == "y":
                    for i, by in enumerate(acceptable):
                        print(by.name, end=',' if i < (
                            len(acceptable)-1) else '\n')

                sys.exit(1)

        elif opt in ('--query'):
            query = arg

    if by == "postplace":
        print(f"Searching for {query} by postcode / place...")
        print(searchByPostcode(query, organisation, select).text)
    elif by == "name":
        print(f"\nSearching for '{query}' by name...\n")
        print(searchByName(query, organisation, select).text)
    elif by == "coord":
        print(f"Searching by {query} coords...")
    elif by == "ods":
        print(f"Searching by {query} ods...")
    else:
        prRed("This should be unreachable - what have you done..")
