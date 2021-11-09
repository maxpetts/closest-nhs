import requests
from dotenv import load_dotenv
from os import getenv
import enum
import json

if load_dotenv(".env"):
    print("""Loaded env variables""")
else:
    print("""
    You need a personal NHS API key.
    Available from: https://developer.api.nhs.uk/register
    """)


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


def constrJSONBody(filter: str, select: str, order: str, top: int, count: bool) -> str:
    """Contstruct a json string of all the required search queries for REST API"""
    body = {"filter": filter, "select": select,
            "orderby": order, "top": top, "count": count}
    return json.dumps(body)


def dispatchRequest(searchQuery: str, reqBody: str, reqHeaders={"subscription-key": getenv("NHSKEY"), "Content-Type": "application/json"}) -> requests.Response:
    """Dispatch a post request to the NHS search postcode-or-place url."""
    # Should I strip REST request queries?
    url = "https://api.nhs.uk/service-search/search-postcode-or-place?api-version=1&search=" + \
        searchQuery.replace(" ", "")

    print(
        f"Dispatching with headers: {reqHeaders}\n and body content of: {reqBody}")
    res = requests.post(url, headers=reqHeaders, data=reqBody)
    return res


if __name__ == "__main__":
    # TODO: parse inp args to constrJSONBody
    searchQuery = "b90"
    body = constrJSONBody("(OrganisationTypeID eq 'DEN')",
                          "OrganisationName,Address1,Address2,Address3,Postcode", "OrganisationName", 2, False)
    print(dispatchRequest(searchQuery, body).text)
#     response = requests.post(
#         url='https://api.nhs.uk/service-search/search-postcode-or-place?api-version=1&search=' +
#             searchQuery.replace(" ", ""),
#         headers={
#             'Content-Type': 'application/json',
#             'subscription-key': 'bf1cc75615804b51ba42024449373e5c'
#                 },
#         data=u'''
# {
#     "filter": "(OrganisationTypeID eq 'DEN') or (OrganisationTypeID eq 'OPT') or (OrganisationTypeID eq 'PHA')",
#     "select": "OrganisationName,Address1,Address2,Address3,City,County,Postcode,OpeningTimes,Contacts",
#     "top": 25,
#     "skip": 0,
#     "count": true
# }
#     ''', )

#     print(response.text)
