# closest-nhs

A utility to search for the nearest NHS facility.

_A NHS API Wrapper?_

I do not own any of the data you can recieve through this wrapper/guide.

# Notes

The following guide below is for the nhs-wrap.py file. The other folders are extensions/different use-cases of this file; for seperate use-cases.

# Set-up

_Working as of: 9th Nov 2021_

1. Create a NHS [developer account](https://developer.api.nhs.uk/register).
2. Then go to your dev account [profile](https://developer.api.nhs.uk/profile) & copy your Primary key.
3. Paste your key into a .env file at the root of this project. You can do this using `echo "NHSKEY=|your primary key|" > .env` - of course replace the pipes(|), and text inside them, with your personal key.
4. Install the dependencies using pip3: `pip3 install python-dotenv requests`.

**OR**

1. Type `make setup` into terminal at the root folder of this project.
2. Enter your API Key.
3. Wait for pip to install dependencies then continue to [usage](#usage)

# Usage

After following the steps in the set-up section above, enter the following into your terminal of choice:
`$ python3 nhs-wrap.py`.
You must be within the root folder of this project.

## Options

Typical program call:

**Short:** `$ python3 nhs-wrap.py -oDentist,ClinCommisGrp -sName,Address,OpenTimes -bname --query"The Ivy"`

**Long:** `$ python3 nhs-wrap.py --organisation=Dentist,ClinCommisGrp --select=Type,Name,Address,OpenTimes --by=name --query="The Ivy"`

| Short Form | Long Form        | Argument                                    |
| ---------- | ---------------- | ------------------------------------------- |
| `-o`       | `--organisation` | [Organisation Types](###Organisation-types) |
| `-s`       | `--select`       | [Selection Types](###Selection-types)       |
| `-b`       | `--by`           | coord, postplace, name, ods                 |
|            | `--query`        | _Depends upon `-b`_                         |

The argument passed to `-b` _or_ `-by` represents what the API will be polled for: `postplace` allows for seaching by postcode or place name.

If your query contains spaces it must be wrapped in quotes!

### Organisation types

This argument is the complete list of organisation types provided by the NHS, _this could also be considered as a facility type_.
The below list is the direct argument format; minus the minus(-).
Multiple arguments are accepted as comma-seperated strings; without spaces.

- AreaTeam = Area Team
- CareHome = Care homes and care at home
- Clinic = Clinic
- ClinCommisGrp = Clinical Commissioning Group
- Dentist = Dentists
- GP = GP
- GPPractice = GP practice
- GenDirOfServ = Generic Directory of Services
- GenServDir = Generic Service Directory
- HealthAuth = Health Authority
- HealthWell = Health and Wellbeing Board
- Hospital = Hospital
- LocalAuth = Local Authority
- MinorInj = Minor Injury Unit
- Opticians = Opticians
- Pharmacy = Pharmacy
- RegionalArea = Regional Area Team
- SocialProv = Social care provider
- StratHealth = Strategic Health Authority
- Sustain = Sustainability and Transformation Partnership
- Trust = Trust
- UrgentCare = Urgent Care

### Selection types

This argument is an abstracted version of all of the column names within their OpenAPI.
It's only abstracted in the address type, as this contains many different columns: _postcode, city etc_.
The below list is the direct argument format; minus the minus(-).
Multiple arguments are accepted as comma-seperated strings; without spaces.

- Name
- Address
- OpenTimes
- Contact
- Alias
- Type

### Query types

This is the search query you want to poll the API with.
As such the data types have been provided that your input **must** conform to.

| if `-b` = | Argument format                   |
| --------- | --------------------------------- |
| coord     | comma seperated ints : [long,lat] |
| postplace | string: "b90" _OR_ "birmingham"   |
| name      | string: "Queen Elizabeth"         |
| ods       | string: ""                        |

_I'm not sure what an ODS string looks like - if you do please make a pull request with one in the above table_

# Todo

- [x] Get JSON from NHS API
- [ ] Parse JSON data into readble results
- [x] Accept search query as user input
- [x] Allow user to select what Organisation type to search for.
- [ ] GUI
- [ ] Add fallback if API fails - sql database
- [ ] Swap to better architecture (seperate Wrapper & Handler)
- [x] ~~Create better constrJSONBody function~~ Now hardcoded into each `searchBy` function
  - [x] ~~Dont send null body tags/attributes(?)~~ See above
- [ ] Unit tests
