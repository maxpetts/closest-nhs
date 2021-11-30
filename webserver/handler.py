from enum import Enum
from os import getenv
import requests


class organisID(Enum):
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


class selections(Enum):
    Name = "OrganisationName"
    Address = "Address1,Address2,Address3,City,County,Postcode"
    OpenTimes = "OpeningTimes"
    Contact = "Contacts"
    Alias = "OrganisationAliases"
    Type = "OrganisationTypeID"


def dispatchRequest(reqBody: str,
                    url="https://api.nhs.uk/service-search/search/?api-version=1",
                    reqHeaders={"subscription-key": getenv("NHSKEY"), "Content-Type": "application/json"}) -> requests.Response:
    """Dispatch a post request to the NHS search"""

    # Should I strip REST request queries?
    print("URL: " + url)
    print("\nhead: ")
    print(reqHeaders)
    print("\nbody: ")
    print(reqBody)
    print("\n")

    return requests.post(url, headers=reqHeaders, data=reqBody)


def constructFilterStr(orgIDs: str) -> str:

    orgs: list(organisID) = []
    # try catch not element in enum
    for orgID in orgIDs.split(","):
        orgs.append(organisID[orgID])

    return f"OrganisationTypeID eq '{orgs[0].value}'" if len(orgs) == 1 else " or ".join(
        f"(OrganisationTypeID eq '{orgID.value}')" for orgID in orgs)


def constructSelectStr(selections: list(selections)) -> str:
    return ",".join([f"{selection.name}" for selection in selections])
