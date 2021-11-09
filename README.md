# closest-nhs

A utility to get the closest NHS location: GPs, Dentists, Pharmacies etc.

_A NHS API Wrapper?_

# Set-up

_Working as of: 9th Nov 2021_

1. Create a NHS [developer account](https://developer.api.nhs.uk/register)
2. Then go to your dev account [profile](https://developer.api.nhs.uk/profile) & copy your Primary key
3. Paste your key into a .env file at the root of this project. You can do this using `echo "NHSKEY=|your primary key|" > .env` - of course replace the pipes(|), and text inside them, with your personal key.
4. Install the dependencies using pip3: `pip3 install python-dotenv requests`

**OR**

1. Type `make setup` in root folder of project

# Usage

After following the steps in the set-up section above, enter the following into your terminal of choice:
`$ python3 getData.py `.
You must be within the root folder of this project.

## Options

Typical program call: `$ python3 getData.py -oDentist -sName,Address -bname

| Short Form | Long Form  | Argument                                    |
| ---------- | ---------- | ------------------------------------------- |
| `-o`       | `-organis` | [Organisation Types](###Organisation-types) |
| `-s`       | `-select`  | [Selection Types](###Selection-types)       |
| `-b`       | `-by`      | coord, postplace, name, ods                 |
| `-q`       | `-query`   | _Depends upon `-b`_                         |

The argument passed to `-b` _or_ `-by` represents what the returned data will be sorted by

### Organisation types

This argument is the complete list of organisation types provided by the NHS.
The below list is the direct argument format; minus the minus(-).

- AreaTeam
- CareHome
- Clinic
- ClinCommisGrp
- Dentist
- GP
- GPPractice
- GenDirOfServ
- GenServDir
- HealthAuth
- HealthWell
- Hospital
- LocalAuth
- MinorInj
- Opticians
- Pharmacy
- RegionalArea
- SocialProv
- StratHealth
- Sustain
- Trust
- UrgentCare

### Selection types

This argument is an abstracted version of all of the column names within their OpenAPI.
It's only abstracted in the address type, as this contains many different columns: _postcode, city etc_.
The below list is the direct argument format; minus the minus(-).

- Name
- Address
- OpenTimes
- Contact

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
- [ ] Accept search query as user input
- [ ] Allow user to select what Organisation type to search for.
- [ ] GUI
- [ ] Add fallback if API fails - sql database
- [ ] Swap to better architecture (seperate Wrapper & Handler)
